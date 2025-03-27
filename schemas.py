from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):

    id:Optional[int] = None
    username:str
    email:str
    password:str
    is_staff:Optional[bool] = False
    is_active:Optional[bool] = False


    class Config:
        orm_model = True
        json_schema_extra = {
            'example': {
                "username":"nepal",
                'email':'nepal@gmail.com',
                "password":'password',
                "is_staff":False,
                "is_active":False
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str = ('419a85f839fea048394ad24c2ae9f00b19e95dbaef1a047c70fa3e55558b9756')

    
class LoginModel(BaseModel):
    username:str
    password:str