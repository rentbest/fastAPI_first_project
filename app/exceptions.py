from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = None
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует!"


class IncorrectEmailOrPasswordException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"


class TokenExpireException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"
    

class TokenAbsentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"
