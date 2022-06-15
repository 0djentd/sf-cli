import logging

from sqlalchemy.orm import Session
from sqlalchemy import select

from .core import create_db, Base
from .flashcards import Flashcard


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


engine = create_db()

with Session(engine) as session:
    fcs = select(Flashcard)
    for x in session.scalars(fcs):
        logger.debug(x)
