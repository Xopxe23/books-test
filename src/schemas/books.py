from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    author: str

    class ConfigDict:
        from_attributes = True


class BookCreateSchema(BaseModel):
    title: str
    author: str
