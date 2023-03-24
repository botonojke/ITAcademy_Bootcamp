from fastapi import Depends, HTTPException, status

from repositories.author import AuthorRepository
from repositories.books import BooksRepository

from db.base import database


def get_author_repository() -> AuthorRepository:
    return AuthorRepository(database)


def get_books_repository() -> BooksRepository:
    return BooksRepository(database)
