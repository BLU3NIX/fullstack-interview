from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    name: Optional[str] = None
    order: Optional[int] = None
    completed: Optional[bool] = None


class TodoCreate(BaseModel):
    name: str
    completed: bool


class TodoUpdate(Todo):
    pass


class TodoResponse(BaseModel):
    id: int
    name: str
    order: int
    completed: bool

    class Config:
        from_attributes = True


# class TodoCreateResponse(BaseModel):
#     success: bool
#     created_todo: Optional[TodoResponse] = None
#     error: Optional[str] = None


# class TodoUpdateResponse(BaseModel):
#     success: bool
#     updated_todo: Optional[TodoResponse] = None
#     error: Optional[str] = None


# class TodoDeleteResponse(BaseModel):
#     success: bool
#     deleted_todo: Optional[TodoResponse] = None
#     error: Optional[str] = None
