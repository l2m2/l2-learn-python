from sqlalchemy import create_engine
from models import Base, User, Model1

engine = create_engine('postgresql://postgres:postgres@localhost/sqlalchemy-demo', echo=True)
Base.metadata.create_all(engine)