from fastapi import Depends, HTTPException
from .auth import get_current_user


def authorize(roles: list):
    def checker(user=Depends(get_current_user)):
        if user.role not in roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return checker
