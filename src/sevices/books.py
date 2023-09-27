from src.repositories.books import BooksRepository
from src.schemas.books import BookCreateSchema


class BooksService:
    @classmethod
    async def get_books(cls):
        books = await BooksRepository.list()
        return books

    @classmethod
    async def add_book(cls, book: BookCreateSchema):
        book = await BooksRepository.add(book.model_dump())
        return book

    @classmethod
    async def delete_all(cls):
        await BooksRepository.delete_all()
