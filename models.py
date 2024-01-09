import urllib
from sqlalchemy import Column, Integer, String, Date, create_engine, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# SQLAlchemy models
Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    user_id = Column(Integer,autoincrement=True,index=True,primary_key=True)
    first_name = Column(String(length=255))
    last_name = Column(String(length=255))
    phone_number = Column(String(length=12))
    email = Column(String(length=255))
    insurances = relationship('insurance_data', back_populates='user',cascade='all, delete-orphan')

class insurance_data(Base):
    __tablename__ = "insurance_data"
    policy_holder_id = Column(Integer, index=True,primary_key=True)
    policy_holder_name = Column(String(length=255), unique=True, index=True)
    city = Column(String(length=255), unique=True, index=True)
    country = Column(String(length=255))
    start_date = Column(Date)
    coverage_amount = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    user = relationship('User', back_populates='insurances')

encoded_password = urllib.parse.quote_plus("Sudheer@66")
DATABASE_URL = f"mysql://sudheer:{encoded_password}@localhost:3306/testdb"
engine = create_engine(
    DATABASE_URL
)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
