import sqlalchemy as sa
from sqlalchemy.orm import relationship
from data.sqlalchemybase import BaseClass


class Branch(BaseClass):
    __tablename__ = "branches"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    street = sa.Column(sa.String)
    district = sa.Column(sa.String, index=True)
    phone_no = sa.Column(sa.Integer)

    # Relationship
    books = relationship("Book", back_populates="branch")

    def __repr__(self):
        return f"{self.district}"

