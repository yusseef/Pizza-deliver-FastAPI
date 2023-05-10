from fastapi import APIRouter

auth_router = APIRouter(
    prefix='/auth',
    tags= ['auth']
    )

@auth_router.get('/')
async def hello():
    return {'message': 'Hello from auth'}
'''
@auth_router.ge('/hello')
async def hello2():
    return {}
    '''