from abc import ABC, abstractmethod
from ..models import User

class UserRepository(ABC):
    @abstractmethod
    def get(self, id: int) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
