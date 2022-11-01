from pydantic import BaseModel


class TestPostModel(BaseModel):
    src_lang: str
    dst_lang: str
