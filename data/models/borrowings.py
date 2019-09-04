import datetime
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from data.sqlalchemybase import BaseClass


class Borrowing(BaseClass):
    __tablename__ = "borrowings"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    start_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    end_date = sa.Column(sa.DateTime)

    # Relationships
    # books
    book_id = sa.Column(sa.Integer, sa.ForeignKey("books.id"))
    books = relationship("Book", back_populates="borrowing")
    # client
    client_id = sa.Column(sa.Integer, sa.ForeignKey("clients.id"))
    client = relationship("Client", back_populates="borrowings")

    
    def __repr__(self):
        from services.data_service import book_by_id
        book = book_by_id(self.book_id)
        
        return f'{datetime.date.isoformat(self.start_date)}: ID: {self.id}. Title: {book.title}. Returned on: {self.end_date if self.end_date else "not yet"}'

        
