import datetime
from pydantic import BaseModel


class Books(BaseModel):
    id: int
    author_id: int
    title: str
    description: str
    publishing_time: datetime.datetime
