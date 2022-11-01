from fastapi import APIRouter

from frontend.website.translator import route_translator

api_router = APIRouter()

api_router.include_router(route_translator.router, prefix="", tags=["translate-website"])
