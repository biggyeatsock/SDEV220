from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.title} - {self.author}"
    
@app.route('/') 
def index(): # Home page
    return "Welcome to the Library!!"

@app.route('/books')
def get_books(): # Finds all the books in the database and returns them as a list of dictionaries.
    books = Books.query.all()
    output = []
    for book in books:
        book_data = {'title': book.title, 'author': book.author}
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id): # Finds a book by its ID and returns it as a dictionary.
    book = Books.query.get_or_404(id)
    return {"title": book.title, "author": book.author}

@app.route('/books', methods=['POST'])
def add_book(): # Adds a new book to the database.
    book = Books(title=request.json['title'], author=request.json['author'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id): # Deletes a book from the database.
    book = Books.query.get(id)
    if book is None:
        return {'error': 'not found'}
    db.session.delete(book)
    db.session.commit()
    return {'message': 'deleted'}
