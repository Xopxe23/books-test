from fastapi import APIRouter

from src.schemas.books import BookCreateSchema, BookSchema
from src.sevices.books import BooksService

router = APIRouter(tags=["books"])


@router.get("/")
async def get_books() -> list[BookSchema]:
    books = await BooksService.get_books()
    return books


@router.post("/")
async def create_book(data: BookCreateSchema) -> BookSchema:
    book = await BooksService.add_book(data)
    return book
