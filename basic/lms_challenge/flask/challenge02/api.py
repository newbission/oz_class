from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

bp = Blueprint("books", "books", url_prefix="/books", description="Operations on books")

books = []

# 북리스트 가져오기 입력하기


@bp.route("/")
class BookList(MethodView):
    @bp.response(200, BookSchema(many=True))
    def get(self):
        return books


@bp.route("/new")
class NewBook(MethodView):
    @bp.arguments(BookSchema)
    @bp.response(201, BookSchema)
    def post(self, new_data):
        new_data["id"] = len(books) + 1
        books.append(new_data)
        return new_data


@bp.route("/<int:book_id>")
class Book(MethodView):
    @bp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        return book

    @bp.arguments(BookSchema)
    @bp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        book.update(new_data)
        return book

    @bp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        books = [book for book in books if book["id"] != book_id]
        return ""
