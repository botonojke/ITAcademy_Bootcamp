from typing import List
from models.books import Books
from repositories.books import BooksRepository
from fastapi import APIRouter, Depends, HTTPException, status
from endpoints.depends import get_books_repository

router = APIRouter()


@router.get("/", response_model=List[Books])
async def show_all_books(
        limit: int = 100,
        skip: int = 0,
        book: BooksRepository = Depends(get_books_repository)) -> List[Books]:
    return await book.all_books(limit=limit, skip=skip)


@router.post("/", response_model=Books)
async def create_books(
        books: Books,
        book: BooksRepository = Depends(get_books_repository)) -> Books:
    return await book.create_book(item=books)


@router.put("/", response_model=Books)
async def update_books(
        id: int,
        books: Books,
        book: BooksRepository = Depends(get_books_repository)) -> Books:
    return await book.update_book(id=id, item=books)


@router.delete("/")
async def delete_books(
        id: int,
        book: BooksRepository = Depends(get_books_repository)):
    await book.delete_book(id=id)
    return HTTPException(status_code=status.HTTP_200_OK, detail="Book deleted")
