import pytest
from httpx import AsyncClient

from src.repositories.books import BooksRepository


@pytest.mark.parametrize("title,author,status_code", [
    ("Золотой ключик, или приключения Буратино", "Алексей Толстой", 200),
    ("Маленький Мук", "Вильгельм Гауф", 200)
])
async def test_add_books(title, author, status_code, ac: AsyncClient):
    response = await ac.post("/", json={
        "title": title,
        "author": author
    })
    books = await ac.get("/")
    assert books.status_code == 200
    assert response.status_code == status_code


async def test_list_books():
    books = await BooksRepository.list()
    assert books[0].id == 1
    assert books[0].title == "Сказка о Царе Солтане"
    assert books[1].id == 2
    assert books[1].title == "Сказка о рыбаке и рыбке"


async def test_delete_all():
    books = await BooksRepository.delete_all()
    assert books is None
