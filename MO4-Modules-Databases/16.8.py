import csv
import sqlite3
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String

# 16.1
with open('books.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['author', 'book'])
    writer.writerow(['J R R Tolkien', 'The Hobbit'])
    writer.writerow(['Lynne Truss', 'Eats, Shoots & Leaves'])

# 16.2
with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# 16.3
with open('books2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'author', 'year'])
    writer.writerow(['The Weirdstone of Brisingamen', 'Alan Garner', 1960])
    writer.writerow(['Perdido Street Station', 'China Miéville', 2000])
    writer.writerow(['Thud!', 'Terry Pratchett', 2005])
    writer.writerow(['The Spellman Files', 'Lisa Lutz', 2007])
    writer.writerow(['Small Gods', 'Terry Pratchett', 1992])

# 16.4
conn = sqlite3.connect('books.db')
c = conn.cursor()
c.execute('''CREATE TABLE books
             (title TEXT, author TEXT, year INTEGER)''')

# 16.5
with open('books2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO books VALUES (?, ?, ?)", (row['title'], row['author'], row['year']))
conn.commit()

# 16.6
c.execute("SELECT title FROM books ORDER BY title")
print(c.fetchall())

# 16.7
c.execute("SELECT title, author, year FROM books ORDER BY year")
print(c.fetchall())

# 16.8
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
