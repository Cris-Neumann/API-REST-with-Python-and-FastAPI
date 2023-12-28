from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    def verify_password(form_password, password):
        hashed_password = pwd_context.hash(password)
        return pwd_context.verify(form_password, hashed_password)
