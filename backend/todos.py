from fastapi import (
    APIRouter,
    Depends,
    Request,
)

from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from typing import List

from database import get_db
from models import Todo
from schemas import (
    TodoCreate,
    TodoUpdate,
    TodoResponse,
    TodoCreateResponse,
    TodoUpdateResponse,
    TodoDeleteResponse,
)

router = APIRouter(prefix="/todos", tags=["todos"])


# TODOS
@router.get("/read", response_model=List[TodoResponse])
async def read_todos(
    db: Session = Depends(get_db),
):
    """Retrieve all todos ordered by their order field."""
    todos = db.query(Todo).order_by(Todo.order).all()
    return todos


@router.post("/create", response_model=TodoCreateResponse)
async def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
):
    """Create a new todo item."""

    return


@router.patch("/update/{todo_id}", response_model=TodoUpdateResponse)
async def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
):
    """Update an existing todo item."""

    return


@router.delete("/delete/{todo_id}", response_model=TodoDeleteResponse)
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
):
    """Delete a todo item."""

    return
