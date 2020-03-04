import logging
import sys
import pathlib
from typing import List

from loguru import logger
from app.core.logging import InterceptHandler
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "0.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

PROJECT_NAME = config("PROJECT_NAME", cast=str, default="Boilerplate")

LOG_FILE = config(
    "LOG_FILE", cast=str, default=pathlib.Path("./log/log").absolute()
)

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)

logger.configure(
    handlers=[
        {"sink": sys.stderr, "level": LOGGING_LEVEL},
        {"sink": LOG_FILE, "level": LOGGING_LEVEL},
    ]
)
