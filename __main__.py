from pymongo import MongoClient

from CoordinateSet import CoordinateSet
from MongoDbService import MongoDbService
from Point import Point


CONNECTION_STRING = "mongodb://localhost:27017"

def get_database():
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
    
   coords:CoordinateSet = CoordinateSet()
   coords.points.append(Point(1,1,1))
   coords.points.append(Point(2,2,2))
   
   print(coords.toDict())
   mongo:MongoDbService = MongoDbService(CONNECTION_STRING)
   mongo.connect()
   id = mongo.create(coords)
   print(coords._id)
   getResult = mongo.get(id,type(coords))
   print(getResult)
