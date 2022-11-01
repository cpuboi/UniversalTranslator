from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

from frontend.schemas.languages import LanguageValidator
from frontend.schemas.translation import InputTranslationModel
from frontend.translation_adapter.translation_handler import translation_processor
from frontend.website.translator.language_form import LanguageForm

templates = Jinja2Templates(directory="frontend/website/templates")
router = APIRouter(include_in_schema=False)  # Dont list under /docs


@router.get("/")
async def translate(request: Request, msg: str = None):
    " Change to complete name of language and internally change to ISO"
    languages = list(LanguageValidator.iso_set)

    return templates.TemplateResponse(
        "translate.html", {"request": request, "languages": languages}
    )


@router.post("/")
async def translate(request: Request):
    language_form = LanguageForm(request)
    await language_form.load_data()

    if await language_form.is_valid():
        "Check if input data is valid with pydantic schema"
        input_data = InputTranslationModel(
            input_language=language_form.input_language,
            output_language=language_form.output_language,
            input_text=language_form.input_text)

        try:
            " This error checking should be handled by pydantic but there is an error, to be fixed. "
            LanguageValidator.language_iso_check(LanguageValidator.iso_set, input_data.input_language)
            LanguageValidator.language_iso_check(LanguageValidator.iso_set, input_data.output_language)
        except Exception as e:
            language_form.__dict__.get("errors").append(f"Error: {e}")
            return templates.TemplateResponse("translate.html", language_form.__dict__)

        try:
            " Send data to translation model "
            input_data = await translation_processor(input_data)
            language_form.translated_text = input_data.translated_text

            return templates.TemplateResponse("translation_result.html", language_form.__dict__)
            # If time more than 60sec : Lost in translation
        except Exception as e:
            language_form.__dict__.get("errors").append(f"Error translating data {e}")
            return templates.TemplateResponse("translate.html", language_form.__dict__)
