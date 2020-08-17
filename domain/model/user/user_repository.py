"""
ユーザーリポジトリ．
"""
from abc import ABCMeta, abstractmethod
from typing import List

from .user import UserId, User


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def nextId(self) -> UserId:
        """ Get next user id """
        pass

    @abstractmethod
    def get(self, id_: UserId) -> User:
        """ Get user by id """
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        """ Save user """
        pass

    @abstractmethod
    def delete(self, id_: UserId) -> User:
        """ Delete user """
        pass

    @abstractmethod
    def list_(self) -> List[User]:
        """ List all users """
        pass
