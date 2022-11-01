#!/usr/bin/env python3

"""
The Universal Translator is an offline alternative to web based translation services.

As of now it utilizes the following engines:
m2m100
opus-mt


"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles  # In order to host static files like images
from frontend.core.config import settings # Location of ML models, version names and so on
from frontend.api.router import api_router
from frontend.website.base import api_router as webapp_router



def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)

def configure_static(app):
    app.mount("/static", StaticFiles(directory="frontend/website/static"), name="static")


def start_webserver_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, docs_url=None)
    include_router(app)
    configure_static(app)

    @app.get('/favicon.ico', include_in_schema=False)
    async def get_favicon():
        favicon_path = "frontend/website/static/icons8-intelligence-96.png"
        #favicon_path = "website/static/OCP2.png"
        return FileResponse(favicon_path)

    return app


app = start_webserver_application()

