"""
ユーザーのドメインモデル．
"""
from dataclasses import dataclass
from typing import NewType


UserId = NewType("UserId", str)


@dataclass
class User:
    id_: UserId
    name: str

    def updateName(self, name: str) -> None:
        self.name = name
