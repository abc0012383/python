import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:xxx@x.x.x.x/wudi",
                       encoding='utf-8', echo=True)

Base = declarative_base()  


class User(Base):
    __tablename__ = 'user' 
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (self.name, self.password)

Base.metadata.create_all(engine)  

Session_class = sessionmaker(bind=engine) 
Session = Session_class() 

user_obj = User(name="hahahaha", password="3714")  
print(user_obj.name, user_obj.id)  

Session.add(user_obj) 
print(user_obj.name, user_obj.id) 

#data=Session.query(User).filter_by(name="alex").all()
#print(data[0].name)
#print(data[0].password)

Session.commit() 
