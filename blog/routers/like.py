from fastapi import APIRouter,status,HTTPException,Depends
from ..db import schemas,models 
from ..db.database import get_db
from sqlalchemy.orm import Session
from ..oauth2 import get_current_user
like_router=APIRouter(prefix='/likes',tags=['Likes'])
@like_router.post("/",status_code=status.HTTP_201_CREATED)
def like(like:schemas.BlogLike,db:Session=Depends(get_db),current_user:models.User=Depends(get_current_user)):
    like_query=db.query(models.Like).filter(models.Like.blog_id==like.blog_id,models.Like.user_id==current_user.id)
    found_like=like_query.first()
    if like.dir==1:
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f'user {current_user.id} has already liked the blog {like.blog_id}')
        new_like=models.Like(blog_id=like.blog_id,user_id=current_user.id)
        db.add(new_like)
        db.commit()
        db.refresh(new_like)
        return {"msg":"Successfully liked the blog"}
    else :
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The blog is not already liked by user {current_user.id}")
        like_query.delete(synchronize_session=False)
        db.commit()
        return {"msg":"Like successfully deleted"}