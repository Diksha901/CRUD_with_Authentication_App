from fastapi import APIRouter,Depends,status,Response,HTTPException
from ..db import models,schemas 
from ..db.database import get_db 
from  sqlalchemy.orm import Session
from ..oauth2 import get_current_user
from ..hashing import hash_pwd 
user_router=APIRouter(prefix='/user',tags=['Users'])
@user_router.post('/create',response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):
    hashed_password = hash_pwd(user.password)
    user_data = user.model_dump()
    user_data['password'] = hashed_password
    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user_router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(get_current_user)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} does not exist')
    return user
