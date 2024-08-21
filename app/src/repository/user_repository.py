from ..dao.user_dao import UserDAO
from ..models.user import User
from typing import Optional


class UserRepository:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def find_user(self, user_id: int) -> Optional[User]:
        return self.user_dao.get_user_by_id(user_id)

    def add_user(self, user: User) -> Optional[int]:
        return self.user_dao.create_user(user)
    
    def get_users(self) -> Optional[int]:
        return self.user_dao.get_all_users()
