from copy import deepcopy
from ModelBase import ModelBase


class CoordinateSet(ModelBase):

    def __init__(self):
        ModelBase.__init__(self)
        self.points = []

    def toDict(self) -> dict:
        copy = deepcopy(self)
        copy.points = [x.toDict() for x in copy.points]
        return copy.__dict__