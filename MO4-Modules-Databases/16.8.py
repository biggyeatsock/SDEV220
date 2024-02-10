# 16.8
import sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table

# Create engine
engine = create_engine('sqlite:///books.db')

# Reflect the existing database into MetaData
meta = MetaData()
meta.reflect(bind=engine)

# Access the books table
books_table = Table('books', meta, autoload=True, autoload_with=engine)

# Select and print title column in alphabetical order
with engine.connect() as conn:
    stmt = select([books_table.c.title]).order_by(books_table.c.title)
    results = conn.execute(stmt).fetchall()
    for row in results:
        print(row[0])