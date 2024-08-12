from typing import Optional


class User:
    def __init__(self, id: Optional[int], name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', age={self.age})"
