import uvicorn
from fastapi import FastAPI

from src.api.tasks import router as books_router

app = FastAPI(title="Books API")
app.include_router(books_router)


if __name__ == '__main__':
    uvicorn.run('src.main:app', reload=True)
