"""
ユーザーリポジトリ．
"""
from typing import List

from .user import UserId, User


class IUserRepository:
    def nextId(self) -> UserId:
        """ Get next user id """
        raise NotImplementedError("")

    def get(self, id_: UserId) -> User:
        """ Get user by id """
        raise NotImplementedError("")

    def save(self, user: User) -> None:
        """ Save user """
        raise NotImplementedError("")

    def delete(self, id_: UserId) -> None:
        """ Delete user """
        raise NotImplementedError("")

    def list_(self) -> List[User]:
        """ List all users """
        raise NotImplementedError("")
