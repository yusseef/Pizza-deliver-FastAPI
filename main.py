from fastapi import FastAPI
from auth_routers import auth_router
from order_routers import order_router
app = FastAPI()


app.include_router(auth_router)
app.include_router(order_router)
'''
@app.get('/admin')
async def hello():
    return {"Hello"}
    '''