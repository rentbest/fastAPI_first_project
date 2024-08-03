from fastapi import HTTPException, Request, Depends, status
from jose import jwt, JWTError
from app.users.models import Users
from app.config import settings
from datetime import datetime
from app.users.dao import UsersDAO
from exceptions import (
    TokenExpireException,
    TokenAbsentException,
    IncorrectTokenException,
)


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(jwt_token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            jwt_token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenException

    expire: str = payload.get("exp")
    if (not expire) or (datetime.fromtimestamp(expire) < datetime.utcnow()):
        raise TokenExpireException

    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return current_user
