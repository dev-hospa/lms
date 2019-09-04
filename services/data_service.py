from typing import List
import datetime

from data import session_factory
from data.models.books import Book
from data.models.borrowings import Borrowing
from data.models.branches import Branch
from data.models.clients import Client


def login_client() -> Client:
    session = session_factory.create_session()

    client_id = int(input("choose client id [1 - 20] "))
    client = session.query(Client).filter(Client.id == client_id).first()
    print(client)

    return client


def books_by_title(book_title: str) -> List[Book]:
    session = session_factory.create_session()

    books = session.query(Book).order_by(Book.author).\
            filter(Book.title == book_title).all()

    return list(books)


def books_by_author(author: str) -> List[Book]:
    session = session_factory.create_session()

    books = session.query(Book).order_by(Book.title).\
            filter(Book.author == author).all()

    return list(books)


def book_by_id(idx: int) -> Book:
    session = session_factory.create_session()

    book = session.query(Book).filter(Book.id == idx).one()

    return book


def is_free(book_id: int) -> bool:
    book = book_by_id(book_id)
    availability = book.available

    return availability == "Free"



def create_borrowing(book_id: int, client_id: int) -> Borrowing:
    session = session_factory.create_session()

    borrowing = Borrowing()
    borrowing.book_id = book_id
    borrowing.client_id = client_id
    session.add(borrowing)

    # set the availability to borrowed
    book = session.query(Book).filter(Book.id == book_id).one()
    book.available = "Borrowed"
    session.commit()

    return borrowing


def borrowing_details(borrowing: Borrowing):
    session = session_factory.create_session()

    borrowing = borrowing
    client = session.query(Client).filter(Client.id == borrowing.client_id).one()
    book = book_by_id(borrowing.book_id)

    return f"Client {client.last_name} has borrowed {book.title}"


def list_of_borrowing(client_id: int) -> List[Borrowing]:
    session = session_factory.create_session()

    borrowings = session.query(Borrowing).filter(Borrowing.client_id == client_id).all()

    return borrowings


def opened_borrowings(client_id: int) -> List[Borrowing]:
    session = session_factory.create_session

    borrowings = list_of_borrowing(client_id)
    opened_borrowings = [borrowing for borrowing in borrowings if borrowing.end_date == None]

    return opened_borrowings


def close_borrowing(borrowing_id: int):
    """
    changes the availability of book to free
    and adds the returned date
    """
    session = session_factory.create_session()

    borrowing = session.query(Borrowing).filter(Borrowing.id == borrowing_id).one()
    borrowing.end_date = datetime.datetime.now()

    book = session.query(Book).filter(Book.id == borrowing.book_id).one()
    book.available = "Free"

    session.commit()
    print(borrowing)