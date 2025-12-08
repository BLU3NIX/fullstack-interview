from fastapi import APIRouter, Depends, Request, HTTPException

from sqlalchemy.orm import Session
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
from auth import require_api_key


router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/read", response_model=List[TodoResponse])
@require_api_key
async def read_todos(
    request: Request,
    db: Session = Depends(get_db),
):
    return


@router.post("/create", response_model=TodoCreateResponse)
@require_api_key
async def create_todo(
    request: Request,
    todo: TodoCreate,
    db: Session = Depends(get_db),
):
    return


@router.patch("/update/{todo_id}", response_model=TodoUpdateResponse)
@require_api_key
async def update_todo(
    request: Request,
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
):
    return


@router.delete("/delete/{todo_id}", response_model=TodoDeleteResponse)
@require_api_key
async def delete_todo(
    request: Request,
    todo_id: int,
    db: Session = Depends(get_db),
):
    return
