import uuid
from pymongo import MongoClient
from AbstractDatabase import AbstractDatabase
import ModelBase

class MongoDbService(AbstractDatabase):

    def __init__(self,connectionString:str,dbName:str="ArnesPointDb"):
        self.__connectionString = connectionString
        self.__dbName = dbName


    def connect(self):
        self.__client = MongoClient(self.__connectionString)
        self.__db = self.__client[self.__dbName]


    def get(self,id:str,type:type)-> any:
        return self.__db[type.__name__].find_one({'_id':id})


    def create(self,value:ModelBase)-> str:
        id = self.__db[type(value).__name__].insert_one(value.toDict())
        value._id = id.inserted_id
        return id.inserted_id
        

    def delete(self,id:str,type:type) -> int:
        return self.__db[type.__name__].delete_one({'id':id}).deleted_count

    def update(self,id:str,value:dict):
        return self.__db[type(value).__name__].update_one({'id':id},{"$set":value})