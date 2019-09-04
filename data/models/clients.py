import sqlalchemy as sa
from sqlalchemy.orm import relationship
from data.sqlalchemybase import BaseClass


class Client(BaseClass):
    __tablename__ = "clients"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String, index=True)
    email = sa.Column(sa.String, unique=True, index=True)

    def __repr__(self):
        return f"Client {self.id}: {self.first_name} {self.last_name}"

    # Relationship
    # borrowing_id = sa.Column(sa.Integer, sa.ForeignKey("borrowings.id"))
    borrowings = relationship("Borrowing", back_populates="client")

