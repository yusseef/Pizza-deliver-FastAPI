from pydantic import *
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                "username": "johndoe",
                "email": "johndoe@example.com",
                "password":"password",
                "is_staff": "False",
                "is_active": "False",
            }
        }