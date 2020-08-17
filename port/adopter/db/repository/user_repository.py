"""
ユーザーリポジトリの実装．
"""
from typing import List
from uuid import uuid4


from ...domain.model.user.user_repository import IUserRepository
from ...domain.model.user.user import UserId, User
from ..db import MySQLDatabase


class UserRepository(IUserRepository):
    def __init__(self):
        self._db = MySQLDatabase()

    def nextId(self) -> UserId:
        return UserId(uuid4())

    def get(self, id_: UserId) -> User:
        return self._db.query(User, (
            'SELECT id, name FROM users '
            'WHERE id = %s LIMIT 1'
        ), (id_))[0]

    def save(self, user: User) -> None:
        self._db.command((
            'INSERT INTO users (id, name) '
            'VALUES (%s, %s)'
        ), (user.id_, user.name))

    def delete(self, id_: UserId) -> User:
        self._db.query((
            'DELETE FROM users '
            'WHERE id = %s'
        ), (id_))

    def list_(self) -> List[User]:
        return self._db.query(User, (
            'SELECT id, name FROM users '
        ))
