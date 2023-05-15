from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from schema import UserSchema
from database_setup import Engine, Session
from models import User
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

session = Session(bind=Engine)


@auth_router.get('/')
async def hello():
    return {'message': 'Hello from auth'}
'''
@auth_router.ge('/hello')
async def hello2():
    return {}
    '''

def check_user_exist(value:str, field:str):
    db_user = session.query(User).filter(
        or_(User.email == value, User.username == value)).first()
    if db_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = f"this {field} is already in use")

@auth_router.post('/signup', response_model = UserSchema, status_code = status.HTTP_201_CREATED)
async def signup(user: UserSchema):
    check_user_exist(user.email, 'email')
    check_user_exist(user.username, 'username')
    new_user = User(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff = user.is_staff,
    )

    session.add(new_user)
    session.commit()

    return new_user


