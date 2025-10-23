from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    name: str
    course: str
    email: EmailStr
    phone: int

class StudentCreate(StudentBase):
    pass

class studentUpdate(StudentBase):
    course : str
    email:EmailStr
    phone: int

class StudentResponse(StudentBase):
    roll_no: int

    class Config:
        orm_mode = True

