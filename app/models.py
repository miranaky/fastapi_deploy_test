from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


def to_camel(string: str) -> str:
    return "".join(word.capitalize() for word in string.split("_"))


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
        alias_generator = to_camel


class File(BaseModel):
    name: str
    path: str
    hash: str

    class Config:
        alias_generator = to_camel


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
