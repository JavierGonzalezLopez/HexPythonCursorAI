from ...domain.models import User
from ...domain.ports.repositories import UserRepository

class SQLUserRepository(UserRepository):
    def get(self, id: int) -> User:
        # In a real application, you'd fetch from a database
        return User(id=id, name="John Doe", email="john@example.com")

    def save(self, user: User) -> None:
        # In a real application, you'd save to a database
        print(f"Saving user: {user.name}")
