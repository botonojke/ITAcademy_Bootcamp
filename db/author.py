import sqlalchemy
from db.base import metadata

author = sqlalchemy.Table(
    'author',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('name', sqlalchemy.String),
)
