from abc import ABC, abstractmethod
import uuid

class AbstractDatabase(ABC):



    def __init__(self):
        pass

    @abstractmethod
    def get(self,id:str,type:type)-> any:
        pass

    @abstractmethod
    def create(self,value)-> str:
        pass

    @abstractmethod
    def delete(self,id:str) -> str:
        pass

    @abstractmethod
    def update(self,id:str,value:any):
        pass
