from sqlalchemy import Column, Integer, String, BigInteger
from db import Base


class Student(Base):
    _tablename_ = "students"

    roll_no = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    course = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(BigInteger, nullable=False)