from contextlib import contextmanager

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import postgres_settings as ps
from .logging_config import log

engine = create_engine(
    URL.create(
        drivername='postgresql+psycopg',
        username=ps.USER,
        password=ps.PASS,
        host=ps.HOST,
        port=ps.PORT,
        database=ps.NAME
    )
)


@contextmanager
def get_session():
    session = sessionmaker(bind=engine)()
    log.debug(f'Создана сессия id:{id(session)}')

    try:
        yield session
        if session.dirty or session.new:
            session.commit()
            log.debug(f'Зафиксирована транзакция id:{id(session)}')
    except Exception as e:
        session.rollback()
        log.error(e)
        raise
    finally:
        session.close()
        log.debug(f'Закрыта сессия id:{id(session)}')


Base = declarative_base()
