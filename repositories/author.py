from repositories.base import BaseRepository
from models.author import Author
from typing import List, Optional
from db.author import author


class AuthorRepository(BaseRepository):

    async def create_author(self, item: Author) -> Author:
        authors = Author(
            id=0,
            name=item.name,
        )
        values = {**authors.dict()}
        values.pop("id", None)
        query = author.insert().values(**values)
        authors.id = await self.database.execute(query=query)
        return authors

    async def update_author(self, id: int, item: Author) -> Author:
        authors = Author(
            id=id,
            name=item.name,
        )
        values = {**authors.dict()}
        values.pop("id", None)
        query = author.update().where(author.c.id == id).values(**values)
        await self.database.execute(query=query)
        return authors

    async def all_authors(self, limit: int = 100, skip: int = 0) -> List[Author]:
        query = author.select().limit(limit).offset(skip)
        data = await self.database.fetch_all(query=query)
        return [Author(**item) for item in data]

    async def delete_author(self, id: int):
        query = author.delete().where(author.c.id == id)
        return await self.database.execute(query=query)

    async def get_author_by_id(self, id: int) -> Optional[Author]:
        query = author.select().where(author.c.id == id)
        book = await self.database.fetch_one(query=query)
        if book is None:
            return None
        return Author.parse_obj(book)
