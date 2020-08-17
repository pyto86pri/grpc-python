"""
データベースの実装．
"""
import logging
from typing import TypeVar, Tuple, Optional, List, Callable

import mysql.connector
from mysql.connector import errorcode

T = TypeVar('T')

config = {
    'user': 'user',
    'password': 'password',
    'host': 'host',
}

logger = logging.getLogger()


class MySQLDatabase:
    def __init__(self):
        try:
            self._cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error('Cannnot connect database.')
            else:
                logger.error(err)
        else:
            self._cnx.close()

    def command(self, operation: str, params: Optional[Tuple] = None) -> None:
        cur = self._cnx.cursor()
        try:
            cur.execute(operation, params)
            self._cnx.commit()
        except Exception as e:
            self._cnx.rollback()
            raise e

    def query(self, factory: Callable[[], T],
              operation: str, params: Optional[Tuple] = None) -> List[T]:
        cur = self._cnx.cursor()
        cur.execute(operation, params)
        return [factory(c) for c in cur]
