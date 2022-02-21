from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


def to_camel(string: str) -> str:
    return ''.join(word.capitalize() for word in string.split('_'))

class Position(BaseModel):
    x: int
    y: int


class Node(BaseModel):
    id: str
    moduleType: str
    position: Position
    data: dict | None = None


class Edge(BaseModel):
    sourcePort: str
    targetPort: str


class Job(BaseModel):
    id: str
    name: str
    nodes: list[Node] = []
    edges: list[Edge] = []


class Column(BaseModel):
    name: str 
    type: str 
    is_feature: bool 
    class Config:
        alias_generator=to_camel


class File(BaseModel):
    name: str 
    path: str 
    hash: str 
    column_attributes: list[Column] 
    description: str  | None
    type: str = Field(..., default=".csv")
    class Config:
        alias_generator=to_camel

# class StudentSchema(BaseModel):
#     fullname: str = Field(...)
#     email: EmailStr = Field(...)
#     course_of_study: str = Field(...)
#     year: int = Field(..., gt=0, lt=9)
#     gpa: float = Field(..., le=4.0)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "Jonh Dae",
#                 "email": "john@dae.com",
#                 "course_of_study": "Computer Science",
#                 "year": 2,
#                 "gpa": "2.0",
#             }
#         }


# class UpdateStudentModel(BaseModel):
#     fullname: Optional[str]
#     email: Optional[EmailStr]
#     course_of_study: Optional[str]
#     year: Optional[int]
#     gpa: Optional[float]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "Jonh Dae",
#                 "email": "john@dae.com",
#                 "course_of_study": "Computer Engineering",
#                 "year": 3,
#                 "gpa": "3.4",
#             }
#         }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
