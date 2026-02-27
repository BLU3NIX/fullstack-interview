from sqlalchemy import Column, String, PrimaryKeyConstraint, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Todo(Base):
    __tablename__ = "todos"
    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
        ),
    )
    id = Column(
        Integer(), primary_key=True, autoincrement=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(), nullable=False, default="")
    order: Mapped[int] = mapped_column(Integer(), nullable=False, unique=True)
    completed: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=False)
