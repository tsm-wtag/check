from pydantic import BaseModel,EmailStr
from datetime import datetime

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    user_type: str
    created_at: datetime


class Resources(BaseModel):
    title: str
    user_id: str
    created_at: datetime

class Resource_details(BaseModel):
    resource_id: str
    link: str
    created_at: datetime



