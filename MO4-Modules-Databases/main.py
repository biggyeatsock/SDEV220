# 11.1 & 11.2

from zoo import A
menagerie = A
menagerie.hours()


# Setup for 16.8
import csv
import sqlite3
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///books.db')
metadata = MetaData()
books_table = Table('books', metadata,
                    Column('title', String),
                    Column('author', String),
                    Column('year', Integer))
metadata.create_all(engine)
with engine.connect() as conn:
    stmt = select(books_table.columns.title).order_by(books_table.columns.title)
    result = conn.execute(stmt)
    print(result.fetchall())
