from fastapi import APIRouter,status,HTTPException,Depends,Response
from ..db import models,schemas 
from ..db.database import get_db 
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List 
from .authentication import oauth2

blog_router=APIRouter(prefix='/blogs',tags=['Blogs'])


@blog_router.post('/blogs',response_model=schemas.ShowBlog,status_code=status.HTTP_201_CREATED)
def create_blog(blog:schemas.Blog,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    new_blog=models.Blog(title=blog.title,body=blog.body,owner_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@blog_router.get('/all',response_model=List[schemas.ShowBlog])
def get_blogs(db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    blogs=db.query(models.Blog).all()
    return blogs 

@blog_router.get('/{id}',response_model=schemas.ShowBlog)
def get_blogs(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} does not exist')
    return blog 

@blog_router.get('/',response_model=List[schemas.ShowBlog])
def search_blogs(Search:str="",limit:int=10,skip:int=0, db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    blog=db.query(models.Blog).filter(models.Blog.title.ilike(f"%{Search}%")).limit(limit=limit).offset(skip).all()
    if not blog:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'blog having given Keyword {Search} does not exist')
    return blog 

@blog_router.get('/display/likes',response_model=List[schemas.BlogLikeOut])
def show_likes(id:int, db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    blog=db.query(models.Blog,func.count(models.Like.blog_id).label("likes")).join(
        models.Like,models.Like.blog_id==models.Blog.id,isouter=True).group_by(models.Blog.id).filter(
            models.Blog.id==id).all()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    response_data = []
    for blog_orm_instance, likes_count in blog:
        blog_pydantic_instance = schemas.Blog.model_validate(blog_orm_instance)
        response_data.append(schemas.BlogLikeOut(
            blog=blog_pydantic_instance,
            likes=likes_count
        ))

    return response_data


@blog_router.put('/{id}')
def update_blogs(id:int,blog:schemas.Blog,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    blog_query=db.query(models.Blog).filter(models.Blog.id==id)
    get_blog=blog_query.first()
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} does not exist')
    if get_blog.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform the given action")
    blog_query.update(blog.model_dump(),synchronize_session=False)
    db.commit()
    return {'data':blog} 


@blog_router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destruct(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    blog_query=db.query(models.Blog).filter(models.Blog.id==id)
    get_blog=blog_query.first()
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} does not exist')
    if get_blog.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform the given action")
    blog_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)