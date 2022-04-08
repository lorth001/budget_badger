from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

dir = os.path.dirname(__file__)

engine = create_engine(f'sqlite:///{dir}/budget-badger.db')

@event.listens_for(engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()

Session = scoped_session(sessionmaker(bind=engine))
session = Session()

Base = declarative_base()
Base.query = Session.query_property()
