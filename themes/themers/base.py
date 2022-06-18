from abc import ABC, abstractmethod


class BaseThemer(ABC):
    @classmethod
    @abstractmethod
    def register(name, theme):
        pass

    @classmethod
    @abstractmethod
    def enable(name):
        pass

    @classmethod
    @abstractmethod
    def list():
        pass

    @classmethod
    @abstractmethod
    def transform(theme):
        pass
