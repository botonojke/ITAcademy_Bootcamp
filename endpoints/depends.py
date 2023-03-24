from fastapi import Depends, HTTPException, status

from core.security import JWTBearer, decode_access_token
from repositories.author import AuthorRepository
from repositories.books import BooksRepository

from db.base import database


def get_author_repository() -> AuthorRepository:
    return AuthorRepository(database)


def get_books_repository() -> BooksRepository:
    return BooksRepository(database)
