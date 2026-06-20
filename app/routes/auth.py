from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import Token, LoginRequest
from app.schemas.user import UserCreate, UserOut
from app.services import user_service
from app.core.security import verify_password, create_access_token
from app.db.session import get_db

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=201)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = user_service.get_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return user_service.create(db, user_in)


@router.post("/login", response_model=Token)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = user_service.get_by_email(db, credentials.email)
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
        )
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
