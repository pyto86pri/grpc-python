"""
データベースの実装．
"""
from types import TracebackType
from typing import TypeVar, Tuple, Optional, List, Callable, Type

T = TypeVar("T")


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
