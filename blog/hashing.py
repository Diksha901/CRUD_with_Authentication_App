from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
def hash_pwd(plain_password):
    return pwd_context.hash(plain_password)
def verify_pwd(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
