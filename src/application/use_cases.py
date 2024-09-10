from ..domain.models import User
from ..domain.ports.repositories import UserRepository

class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, name: str, email: str) -> User:
        # In a real application, you'd generate the ID
        new_user = User(id=1, name=name, email=email)
        self.user_repository.save(new_user)
        return new_user

# If using __all__ for explicit exports
__all__ = ['CreateUser']
