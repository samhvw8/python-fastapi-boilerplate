from fastapi import FastAPI
from app.api.errors.http_error import http_error_handler
from app.api.routes.api import router as api_router
from app.core.config import (
    ALLOWED_HOSTS,
    API_PREFIX,
    DEBUG,
    PROJECT_NAME,
)
from app.core.events import (
    create_start_app_handler,
    create_stop_app_handler,
)
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG)

    application.add_middleware(GZipMiddleware)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler(
        "startup", create_start_app_handler(application)
    )
    application.add_event_handler(
        "shutdown", create_stop_app_handler(application)
    )

    application.add_exception_handler(HTTPException, http_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()
