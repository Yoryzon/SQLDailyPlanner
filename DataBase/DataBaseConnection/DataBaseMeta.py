from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from DataBase.DataBaseConfiguration.DataBaseConfiguration import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_PORT

Base = declarative_base()
Engine = create_engine(f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}", echo=False)
SessionFactory = sessionmaker(Engine, autocommit=False)
