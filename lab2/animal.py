from abc import abstractmethod

from pet import Pet


class Animal(Pet):
    """Абстрактное животное: общее состояние и поведение."""

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def happy_birthday(self) -> None:
        self.__age += 1

    @abstractmethod
    def express(self) -> None:
        pass

    @abstractmethod
    def get_age_in_human_years(self) -> int:
        pass

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age
