"""
"""
import logging
from types import TracebackType
from typing import TypeVar, Tuple, Optional, List, Callable, Type

from configparser import ConfigParser
import pymysql.cursors
from retry.api import retry_call

from .db import Database

T = TypeVar("T")

config = ConfigParser()
config.read("../../../config.ini")

logger = logging.getLogger()


class MySQLDatabase(Database):
    def __enter__(self) -> "MySQLDatabase":
        self._cnx = retry_call(
            pymysql.connect,
            fkwargs=config["mysql"],
            delay=1,
            max_delay=120,
            backoff=2,
            logger=logger,
        )
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: TracebackType,
    ) -> None:
        self._cnx.close()

    def command(self, operation: str, params: Optional[Tuple[str, ...]] = None) -> None:
        try:
            with self._cnx.cursor() as cursor:
                cursor.execute(operation, params)
            self._cnx.commit()
        except Exception as e:
            self._cnx.rollback()
            raise e

    def query(
        self,
        factory: Callable[..., T],
        operation: str,
        params: Optional[Tuple[str, ...]] = None,
    ) -> List[T]:
        with self._cnx.cursor() as cursor:
            cursor.execute(operation, params)
            cursor.execute(operation, params)
            return [factory(*c) for c in cursor]
