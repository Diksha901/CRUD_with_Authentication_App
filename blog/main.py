from fastapi import FastAPI 
from .db import models 
from .db.database import engine  
from .routers import blog,user,authentication,like

app=FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.auth_router)
app.include_router(blog.blog_router)
app.include_router(user.user_router)
app.include_router(like.like_router)

