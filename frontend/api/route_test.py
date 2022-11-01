# This is a test module


from fastapi import APIRouter

from frontend.schemas.test import TestPostModel

router = APIRouter()


@router.get("/")
def get_testdata():
    return {"msg": "OK"}


@router.post("/post/{extra}")  # , response_model=TestResponseModel)
def post_testdata(language_data: TestPostModel, extra: str = None):
    language_data.__dict__.update({"extra": extra})
    return language_data
