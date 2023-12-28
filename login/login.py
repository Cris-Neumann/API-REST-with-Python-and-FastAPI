from security.hashing import Hasher
from security.security import create_access_token
from database.database import get_db
from database.models import User
from database.schemas import Token
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
router = APIRouter()

def get_user(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user

def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email=email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password_):
        return False
    return user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o clave incorrecto")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
