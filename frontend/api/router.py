"""
This is where all different sites will get routed correctly.
"""

from fastapi import APIRouter

from frontend.api import route_test, route_translation

api_router = APIRouter()

api_router.include_router(route_translation.router, prefix="/translate", tags=["translator"])
api_router.include_router(route_test.router, prefix="/test", tags=["test"])
