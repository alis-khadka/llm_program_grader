import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

basedir = os.path.abspath(os.path.dirname(__file__))
DB_FILE = f'sqlite:///{os.path.join(basedir, "./db/grader.db")}'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=False)

# Session factory
SessionLocal = sessionmaker(bind=engine)

# Create tables (can be run on app startup)
def init_db():
    Base.metadata.create_all(engine)

def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = {**kwargs}
        if defaults:
            params.update(defaults)
        instance = model(**params)
        session.add(instance)
        session.commit()
        return instance

