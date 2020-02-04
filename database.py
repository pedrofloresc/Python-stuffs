
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "Usuarios"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name, id):
        self.id = id
        self.name = name
    # def __repr__(self):
    #  return "<User(name='%s', id='%i')>" % (self.name, self.id)


# an Engine, which the Session will use for connection
# resources http://127.0.0.1:58427/
some_engine = create_engine(
    'postgresql://Prouser:123123@localhost/test', echo=True)

#meta = MetaData()

""" Usuarios = Table(
    'Usuarios', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
) """

# meta.create_all(some_engine)

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()
#session = Session.object_session(Usuario)
session.add(Usuario("mariela", "30"))
session.commit()
query = session.query(Usuario).order_by(Usuario.id)
query = query.limit(2)

for q in query:
    print(str(q.id) + q.name)

print(query.count())
# work with sess
#myobject = Usuario(1, "pedro")

# session.add(myobject)
# session.commit()
