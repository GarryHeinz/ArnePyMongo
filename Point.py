from ModelBase import ModelBase


class Point():

    def __init__(self,x:float,y:float,z:float):
        self.x = x
        self.y = y
        self.z = z

    def toDict(self):
        return self.__dict__