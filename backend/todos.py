from fastapi import (
    APIRouter,
    Depends,
    # Request,
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


@router.post("/create")
async def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
):
    """Create a new todo item."""
    try:
        # Calculate order: use provided order or append to end
        max_order = db.query(Todo).order_by(desc(Todo.order)).first()
        new_order = max_order.order + 1 if max_order else 1
        new_todo = Todo(
            name=todo.name or "",
            order=new_order,
            completed=todo.completed or False,
        )
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)

        return TodoCreateResponse(
            success=True,
            created_todo=new_todo,
        )
    except Exception as e:
        db.rollback()
        return TodoCreateResponse(
            success=False,
            error=str(e),
        )
    return


@router.patch("/update/{todo_id}")
async def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
):
    """Update an existing todo item."""
    try:
        existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not existing_todo:
            return TodoUpdateResponse(
                success=False,
                error=f"Todo with id {todo_id} not found",
            )

        # Update only provided fields
        if todo.name is not None:
            existing_todo.name = todo.name
        if todo.order is not None:
            existing_todo.order = todo.order
        if todo.completed is not None:
            existing_todo.completed = todo.completed

        db.commit()
        db.refresh(existing_todo)

        return TodoUpdateResponse(
            success=True,
            updated_todo=existing_todo,
        )
    except Exception as e:
        db.rollback()
        return TodoUpdateResponse(
            success=False,
            error=str(e),
        )
    return


@router.delete("/delete/{todo_id}")
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
):
    """Delete a todo item."""
    try:
        existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not existing_todo:
            return TodoDeleteResponse(
                success=False,
                error=f"Todo with id {todo_id} not found",
            )

        # Store todo data before deletion for response
        deleted_todo = TodoResponse(
            id=existing_todo.id,
            name=existing_todo.name,
            order=existing_todo.order,
            completed=existing_todo.completed,
        )

        db.delete(existing_todo)
        db.commit()

        return TodoDeleteResponse(
            success=True,
            deleted_todo=deleted_todo,
        )
    except Exception as e:
        db.rollback()
        return TodoDeleteResponse(
            success=False,
            error=str(e),
        )
    return
