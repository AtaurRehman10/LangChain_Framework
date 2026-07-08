from typing import TypedDict

class TypedDist(TypedDict):
     name: str
     aga : int 
     salary: float

def create_typed_dict(name: str, age: int, salary: float) -> TypedDist:
     return TypedDist(name=name, aga=age, salary=salary)

personData = create_typed_dict("John Doe", 30, 50000.0)
print(personData)       