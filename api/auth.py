from fastapi import APIRouter, Depends, HTTPException, Response
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

router = APIRouter(prefix='/auth', tags=['Пользователь'])

conf = AuthXConfig()
conf.JWT_ACCESS_COOKIE_NAME = 'my_coockie'
conf.JWT_SECRET_KEY = 'SECRET'
conf.JWT_TOKEN_LOCATION = ['cookies']

security = AuthX(config=conf)

class UserAuth(BaseModel):
    password: str
    name: str

@router.get('/admin')
async def protected(dependency=Depends(security.access_token_required)):
    return {'data': 'You are an admin'}

@router.post('/')
async def auth_user(credentials: UserAuth, resp: Response):
    if credentials.password == 'admin' and credentials.name == 'admin':
        token = security.create_access_token(uid='1')
        resp.set_cookie(conf.JWT_ACCESS_COOKIE_NAME, token)
        return {'acces_token': token}
    raise HTTPException(401, detail='No such user with this password')