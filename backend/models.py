from pydantic import BaseModel

class User(BaseModel):
    ID: str
    PhoneNumber: str
    Name: str
    Address: str
