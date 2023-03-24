from typing import List
from models.author import Author
from repositories.author import AuthorRepository
from fastapi import APIRouter, Depends, HTTPException, status
from endpoints.depends import get_author_repository

router = APIRouter()


@router.get("/", response_model=List[Author])
async def show_all_posts(
        limit: int = 100,
        skip: int = 0,
        author: AuthorRepository = Depends(get_author_repository)) -> List[Author]:
    return await author.all_authors(limit=limit, skip=skip)


@router.post("/", response_model=Author)
async def create_author(
        authors: Author,
        author: AuthorRepository = Depends(get_author_repository)) -> Author:
    return await author.create_author(item=authors)


@router.put("/", response_model=Author)
async def update_author(
        id: int,
        authors: Author,
        author: AuthorRepository = Depends(get_author_repository)) -> Author:
    return await author.update_author(id=id, item=authors)


@router.delete("/")
async def delete_author(
        id: int,
        author: AuthorRepository = Depends(get_author_repository)):
    await author.delete_author(id=id)
    return HTTPException(status_code=status.HTTP_200_OK, detail="Author deleted")
