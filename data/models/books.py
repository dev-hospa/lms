import sqlalchemy as sa
from sqlalchemy.orm import relationship
from data.sqlalchemybase import BaseClass


class Book(BaseClass):
    __tablename__ = "books"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, index=True)
    author = sa.Column(sa.String, index=True)
    year = sa.Column(sa.Integer)
    available = sa.Column(sa.String, default="Free")

    def __repr__(self):
        return f"{self.title} by {self.author}. Branch: {self.branch}. {self.available}"
    
    # Relationship
    branch_id = sa.Column(sa.Integer, sa.ForeignKey("branches.id"))
    branch = relationship("Branch", back_populates="books")

    borrowing = relationship("Borrowing", back_populates="books")