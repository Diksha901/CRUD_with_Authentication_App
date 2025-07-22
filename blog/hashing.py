# from passlib.context import CryptContext
# pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
# class Hash:
#     def encryptPass(pwd):
#         return pwd_context.hash(pwd)
#     def verify(hashed_password,plain_password):
#         return pwd_context.verify(hashed_password,plain_password)
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
def hash_pwd(plain_password):
    return pwd_context.hash(plain_password)
def verify_pwd(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
