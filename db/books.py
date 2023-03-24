import sqlalchemy
import datetime
from db.base import metadata

books = sqlalchemy.Table(
    'books',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('author_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('author.id'), nullable=False),
    sqlalchemy.Column('title', sqlalchemy.String),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('publishing_time', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)

