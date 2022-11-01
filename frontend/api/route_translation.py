from fastapi import APIRouter

from frontend.schemas.translation import ReturnTranslation, InputTranslationModel
from frontend.translation_adapter.translation_handler import translation_processor

router = APIRouter()


@router.post("/", response_model=ReturnTranslation)
def translate_text(input_model: InputTranslationModel):
    translation = translation_processor(input_model)
    return translation
