from sqlalchemy import Column, Integer, String, ForeignKey, JSON

from ..database import Base


class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String, ForeignKey("users.username"), nullable=False)
    tag = Column(String)
    title = Column(String)
    contents = Column(String)
    date = Column(String)
    link = Column(String, nullable=True)
    image = Column(String, nullable=True)
