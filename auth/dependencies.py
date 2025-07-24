# 토큰 검증

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from db.session import SessionLocal
from models.user import User

# JWT 설정
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# OAuth2 스킴: 토큰을 헤더에서 가져오게 설정
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # 로그인 경로

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 실제 인증된 유저를 가져오는 의존성 함수
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception

    return user
