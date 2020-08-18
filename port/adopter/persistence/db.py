"""
データベースの実装．
"""
import logging
from types import TracebackType
from typing import TypeVar, Tuple, Optional, List, Callable, Type

from configparser import ConfigParser
import mysql.connector

T = TypeVar("T")

config = ConfigParser()
config.read("../../../config.ini")

logger = logging.getLogger()


class Database:
    def __enter__(self) -> "Database":
        raise NotImplementedError("")

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: TracebackType,
    ) -> None:
        raise NotImplementedError("")

    def command(self, operation: str, params: Optional[Tuple[str, ...]] = None) -> None:
        raise NotImplementedError("")

    def query(
        self,
        factory: Callable[..., T],
        operation: str,
        params: Optional[Tuple[str, ...]] = None,
    ) -> List[T]:
        raise NotImplementedError("")

    def close(self) -> None:
        raise NotImplementedError("")


class MySQLDatabase(Database):
    def __enter__(self) -> "MySQLDatabase":
        self._cnx = mysql.connector.connect(**config["mysql"])
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: TracebackType,
    ) -> None:
        self._cnx.close()

    def command(self, operation: str, params: Optional[Tuple[str, ...]] = None) -> None:
        cur = self._cnx.cursor()
        try:
            cur.execute(operation, params)
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
        cur = self._cnx.cursor()
        cur.execute(operation, params)
        return [factory(*c) for c in cur]
