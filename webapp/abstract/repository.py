from abc import ABC, abstractmethod
from typing import Any


class ABaseRepository(ABC):

    @abstractmethod
    def add_one() -> None:
        raise NotImplementedError

    @abstractmethod
    def get_one() -> Any | None:
        raise NotImplementedError


class ASetRepository(ABC):

    @abstractmethod
    def get_many() -> list[Any]:
        raise NotImplementedError


class AIDRepository(ABC):

    @abstractmethod
    def get_by_id() -> Any | None:
        raise NotImplementedError

    @abstractmethod
    def exists() -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def update_one() -> Any:
        raise NotImplementedError

    @abstractmethod
    def delete_one() -> bool:
        raise NotImplementedError


class AORMRepository(ABC):
    @abstractmethod
    def merge() -> None:
        raise NotImplementedError

    @abstractmethod
    def flush() -> None:
        raise NotImplementedError

    @abstractmethod
    def commit() -> None:
        raise NotImplementedError


class AReturningRepository(ABC):

    @abstractmethod
    def add_n_return() -> Any:
        raise NotImplementedError


class ACountingRepository(ABC):

    @abstractmethod
    def count() -> int:
        raise NotImplementedError
