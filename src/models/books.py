from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base
from src.schemas.books import BookSchema


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)

    def to_read_model(self):
        return BookSchema(
            id=self.id,
            title=self.title,
            author=self.author
        )
