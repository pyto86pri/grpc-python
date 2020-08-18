"""
ユーザーリポジトリの実装．
"""
from typing import List
from uuid import uuid4


from domain.model.user.user_repository import IUserRepository
from domain.model.user.user import UserId, User
from port.adopter.persistence.db import Database


class UserRepository(IUserRepository):
    def __init__(self, db: Database) -> None:
        self._db = db

    def nextId(self) -> UserId:
        return UserId(str(uuid4()))

    def get(self, id_: UserId) -> User:
        return self._db.query(
            User, ("SELECT id, name FROM users " "WHERE id = %s LIMIT 1"), (id_,)
        )[0]

    def save(self, user: User) -> None:
        self._db.command(
            ("INSERT INTO users (id, name) " "VALUES (%s, %s)"), (user.id_, user.name,)
        )

    def delete(self, id_: UserId) -> None:
        self._db.command(("DELETE FROM users " "WHERE id = %s"), (id_,))

    def list_(self) -> List[User]:
        users: List[User] = self._db.query(User, ("SELECT id, name FROM users "))
        return users
