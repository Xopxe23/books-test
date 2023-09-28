import asyncio
import json

import pytest
from sqlalchemy import insert

from src.config import settings
from src.db import Base, async_session_maker, engine
from src.models.books import Book


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"src/tests/mock_{model}.json", "r") as file:
            return json.load(file)

    books = open_mock_json('books')

    async with async_session_maker() as session:
        add_books = insert(Book).values(books)
        await session.execute(add_books)
        await session.commit()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
