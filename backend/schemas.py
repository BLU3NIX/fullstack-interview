from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    pass


class TodoCreate(Todo):
    pass


class TodoUpdate(Todo):
    pass


class TodoResponse(BaseModel):
    pass


class TodoCreateResponse(BaseModel):
    pass


class TodoUpdateResponse(BaseModel):
    pass


class TodoDeleteResponse(BaseModel):
    pass
