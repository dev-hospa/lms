import sqlalchemy as sa
import sqlalchemy.orm
from db_engine import db_url


engine = None
factory = None

def global_init():
     global engine, Session

     if factory:
          return

     engine = sa.create_engine(db_url)
     Session = sa.orm.sessionmaker(bind=engine)


def create_tables():
     if not engine:
          raise Exception("you haven't called global_init()")

     import data.__all_models
     from data.sqlalchemybase import BaseClass
     BaseClass.metadata.create_all(engine)


def create_session() -> sqlalchemy.orm.Session:
     if not Session:
          raise Exception("you haven't called global_init()")

     session = Session()
     session.expire_on_commit = False
     return session