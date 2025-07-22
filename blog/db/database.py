from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from ..config import settings 
URL_PATH=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine=create_engine(URL_PATH)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()
Base.metadata.create_all(bind=engine)
db=SessionLocal()
def get_db():
    try:
        yield db 
    finally:
        db.close()
