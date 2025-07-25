from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..db import schemas,models
from ..db.database import get_db 
from .. import oauth2,hashing
auth_router=APIRouter(tags=['Authenticate'])
@auth_router.post('/login',response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid Credentials')
    if not hashing.verify_pwd(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    access_token=oauth2.create_access_token(data={"user_id":str(user.id)})
    return {"access_token":access_token,"token_type":'bearer'}
