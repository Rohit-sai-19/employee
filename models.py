from sqlalchemy import Column, Integer, String
from database import Base

class Emp(Base):
    __tablename__ = 'emp'
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email_id = Column(String)
    login = Column(String)
    logout = Column(String)

class Log(Base):
    __tablename__ = 'emp_log'
    
    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String)
    date = Column(String)
    login = Column(String)
    logout = Column(String)

class EmpLog(Base):
    __tablename__ = 'employee_id'  # This is the name of the table in the database
    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(String)  # Email should probably be unique
    password = Column(String)
