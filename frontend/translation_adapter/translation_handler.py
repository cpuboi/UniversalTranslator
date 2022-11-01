import json

import aiohttp

from frontend.core.config import Settings
from frontend.schemas.translation import InputTranslationModel


async def translation_processor(input_model: InputTranslationModel):
    async def post_model(payload, url: str = Settings.TRANSLATION_URL, url_path: str = Settings.TRANSLATION_PATH,
                         port: int = Settings.TRANSLATION_PORT):
        async with aiohttp.ClientSession() as session:
            url_str = f"http://{url}:{str(port)}/{url_path}"
            async with session.post(url_str, json=payload) as resp:
                return await resp.text()

    # send model to ML process.

    response_text = await post_model(input_model.dict())

    input_model.translated_text = json.loads(response_text)["translated_text"]

    return input_model
