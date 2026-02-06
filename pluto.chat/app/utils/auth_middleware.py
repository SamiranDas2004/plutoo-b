from fastapi import Cookie, HTTPException
from app.utils.jwt_handler import decode_token
import logging

logger = logging.getLogger(__name__)


async def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Missing token")

    payload = decode_token(access_token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload
