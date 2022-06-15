from typing import List, Optional
from pydantic import BaseModel

# schemas models means pydantic model

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    
    class Config():
        orm_mode = True


class Users(BaseModel):
    name:str
    email:str
    password:str



class ShowUsers(BaseModel):
    name:str
    email:str
    blogs:List[Blog] = []
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title:str
    body:str
    creator: ShowUsers
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str
    
    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    email:Optional[str] = None