from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional

class Emp(BaseModel):
    first_name: str
    last_name: str
    email_id: str

    class Config:
        orm_mode = True

class EmpList(BaseModel):
    employees: List[Emp]

    class Config:
        orm_mode = True

class EmpLog(BaseModel):
    email_id: str
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

    class Config:
        orm_mode = True
