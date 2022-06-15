import logging
import datetime
import sqlalchemy

from . core import Base


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Flashcard(Base):
    __tablename__ = "flashcard"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    front = sqlalchemy.Column(sqlalchemy.Text)
    back = sqlalchemy.Column(sqlalchemy.Text)
