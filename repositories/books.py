from repositories.base import BaseRepository
from models.books import Books
import datetime
from typing import List, Optional
from db.books import books


class BooksRepository(BaseRepository):

    async def create_book(self, item: Books) -> Books:
        book = Books(
            id=0,
            author_id=item.author_id,
            publishing_time=datetime.datetime.utcnow(),
            title=item.title,
            description=item.description,
        )
        values = {**book.dict()}
        values.pop("id", None)
        query = books.insert().values(**values)
        book.id = await self.database.execute(query=query)
        return book

    async def update_book(self, id: int, item: Books) -> Books:
        book = Books(
            id=id,
            author_id=item.author_id,
            publishing_time=datetime.datetime.utcnow(),
            title=item.title,
            description=item.description,
        )
        values = {**book.dict()}
        values.pop("id", None)
        query = books.update().where(books.c.id == id).values(**values)
        await self.database.execute(query=query)
        return book

    async def all_books(self, limit: int = 100, skip: int = 0) -> List[Books]:
        query = books.select().limit(limit).offset(skip)
        data = await self.database.fetch_all(query=query)
        return [Books(**item) for item in data]

    async def delete_book(self, id: int):
        query = books.delete().where(books.c.id == id)
        return await self.database.execute(query=query)

    async def get_book_by_id(self, id: int) -> Optional[Books]:
        query = books.select().where(books.c.id == id)
        book = await self.database.fetch_one(query=query)
        if book is None:
            return None
        return Books.parse_obj(book)
