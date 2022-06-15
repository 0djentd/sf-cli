import logging

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


Base = declarative_base()


def create_db(db_file: str = "/db.sqlite3") -> Engine:
    db_file = "sqlite://" + db_file
    logger.info(f"Creating db at {db_file}")
    engine = create_engine(db_file, echo=True)
    Base.metadata.create_all(engine)
    return engine
