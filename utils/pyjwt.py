from typing import Callable, Any
from flask import request, jsonify
from utils.config import Config

import jwt


class PyJWT:
    @classmethod
    def encodeToken(cls, userInDb, key) -> str:
        token = jwt.encode(
            payload={
                "username": userInDb.get("username"),
                "email": userInDb.get("email"),
            },
            key=key,
            algorithm="HS256",
        )
        return token

    @classmethod
    def decodeToken(cls, token, key) -> dict:
        return jwt.decode(token, key, algorithms=["HS256"])


def auth(old_function: Callable) -> Callable:
    def wrapper(*args) -> Any:
        token = request.headers.get("Authorization")
        if token == None:
            return jsonify({"status": False, "error": "Authorization Failed"})
        else:
            userEmail = PyJWT.decodeToken(token, Config.JWT_KEY).get("email")
            if userEmail == None:
                return jsonify({"status": False, "error": "Invalid Token"})
            else:
                return old_function(*args, userEmail)

    return wrapper
