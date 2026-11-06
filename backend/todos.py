from fastapi import (
    APIRouter,
    Depends,
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

    last_todo = db.query(Todo).order_by(desc(Todo.order)).first()

    new_todo = Todo(
        name=todo.name,
        completed=todo.completed,
        order=last_todo.order + 1 if last_todo else 1,
    )

    try:
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
    except Exception as e:
        return TodoCreateResponse(success=False, error=str(e))
    
    return TodoCreateResponse(success=True, created_todo=TodoResponse.from_orm(new_todo))


@router.patch("/update/{todo_id}")
async def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
):
    """Update an existing todo item."""
    return


@router.delete("/delete/{todo_id}")
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
):
    """Delete a todo item."""
    return
