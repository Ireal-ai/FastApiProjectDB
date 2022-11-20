from fastapi import FastAPI
from src.views import view_documents_requests, view_rights_requests


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(
        view_documents_requests.documents_router,
        prefix="",
        tags=["view"],
    )

    app.include_router(
        view_rights_requests.rights_router,
        prefix="",
        tags=["view"],
    )
    return app
