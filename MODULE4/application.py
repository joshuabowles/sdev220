from flask import Flask, request
from flask_sqlalchemy import SQLALchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLALchemy(app)


class Book(db.model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404()
    return {"book_name": book.book_name, "author": book.author,'publisher': book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}