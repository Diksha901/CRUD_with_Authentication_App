from typing import Optional,List,Annotated
from pydantic import BaseModel,Field,ConfigDict,EmailStr
class BlogBase(BaseModel):
    title:str 
    body:str 
 
class Blog(BlogBase):
    model_config = ConfigDict(from_attributes=True)

class User(BaseModel):
    id:int
    name:str 
    email:EmailStr 
    password:str 

class UserIn(BaseModel):
    name:str 
    email:EmailStr
    password:str
    

class ShowUser(BaseModel):
    name:str 
    email:EmailStr
    blogs:List[Blog] =[]
    model_config = ConfigDict(from_attributes=True)

class ShowBlog(Blog):
    title:str 
    body:str
    owner:ShowUser
    model_config = ConfigDict(from_attributes=True)

class Login(BaseModel):
    username: str
    password:str

class BlogLike(BaseModel):
    blog_id:int 
    dir : Annotated[int,Field(le=1)]
    model_config = ConfigDict(from_attributes=True)
    
class BlogLikeOut(BaseModel):
    blog:Blog
    likes:int 
    model_config=ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
