from pydantic import BaseModel, Field , EmailStr

class User(BaseModel):
     name: str = Field(..., description="The name of the user")
     age: int = Field(..., ge=0, description="The age of the user")
     email: EmailStr = Field(..., description="The email address of the user")
     salary: float = Field(..., gt=10000, description="The salary of the user")

user = User(name="John Doe", age=30, email="Ata@gmail.com", salary=50000.0)
print(user)