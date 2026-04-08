from fastapi import APIRouter, HTTPException
from app.db.database import SessionLocal
from app.db.models import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import Depends


router = APIRouter(tags=["Auth"])


@router.post("/auth/register")
def register(user: UserCreate):
    db = SessionLocal()

    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()

    return {"message": "User registered"}


@router.post("/auth/login")
def login(email: str, password: str):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"id": user.id, "role": user.role})

    return {
        "access_token": token,
        "token_type": "bearer"
    }