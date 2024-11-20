from abc import ABC, abstractmethod
import uuid

class ModelBase(ABC):

    def __init__(self):
        self._id:str

    @abstractmethod
    def toDict(self)-> dict:
        pass


