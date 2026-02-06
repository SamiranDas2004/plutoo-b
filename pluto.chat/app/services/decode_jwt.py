# import bcrypt
# import jwt
# from datetime import datetime, timedelta
# from app.core.config import settings
# import uuid
# import os
# from dotenv import load_dotenv
# from fastapi import Cookie, HTTPException
# from typing import Optional
# load_dotenv()


# def decode_jwt(token: str): 
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#         return payload
#     except jwt.ExpiredSignatureError:
#         return None
#     except jwt.InvalidTokenError:
#         return None
    

# def get_current_user_from_cookie(access_token: Optional[str] = Cookie(None)):
#     """Extract and validate JWT from httpOnly cookie"""
#     if not access_token:
#         raise HTTPException(status_code=401, detail="Not authenticated")
    
#     payload = decode_jwt(access_token)
#     if not payload:
#         raise HTTPException(status_code=401, detail="Invalid token")
    
#     return payload.get("sub")
