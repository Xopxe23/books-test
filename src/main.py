from fastapi import FastAPI

from src.api.tasks import router as books_router

app = FastAPI(title="Books API")
app.include_router(books_router)
