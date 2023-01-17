from typing import List, Optional

from fastapi import Request


class LanguageForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.input_language: Optional[str] = None
        self.output_language: Optional[str] = None
        self.input_text: Optional[str] = None
        self.translated_text: Optional[str] = None
        self.translation_model: Optional[str] = "default"

    async def load_data(self):
        form = await self.request.form()
        self.input_language = form.get("inputLanguage")
        self.output_language = form.get("outputLanguage")
        self.input_text = form.get("inputText")


    async def is_valid(self):
        if not self.input_text:
            self.errors.append("No input text submitted")
        if not self.errors:
            return True
        return False
