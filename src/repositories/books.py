from sqlalchemy import delete, insert, select

from src.db import async_session_maker
from src.models.books import Book


class BooksRepository:
    @classmethod
    async def add(cls, data: dict):
        query = insert(Book).values(**data).returning(Book)
        async with async_session_maker() as session:
            new_book = await session.execute(query)
            await session.commit()
        result = new_book.scalar_one().to_read_model()
        return result

    @classmethod
    async def list(cls):
        query = select(Book)
        async with async_session_maker() as session:
            books = await session.execute(query)
        result = [row[0].to_read_model() for row in books.all()]
        return result

    @classmethod
    async def delete_all(cls):
        query = delete(Book)
        async with async_session_maker() as session:
            await session.execute(query)
            await session.commit()
