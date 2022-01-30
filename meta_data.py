from dataclasses import dataclass
from typing import List
from type import Type
from segment import Segment

"""
    This class holds the information about the space and its partition to segments.
    ...
    
    Attributes
    ----------
    d : int
        The dimension of the space.
    
    segments : List[Segment]
        A list of non-overlapping segments. Each segment is defined by its boundaries and holds a linear function.
    
    type : Type(ENUM)
        The type of labels needs to be recognized by the Citron tree.
        The type is either categorical, continuous, or binary.
    
    Methods : 
    -------
    d()
        Returns the dimension of the space.
        
    segments()
        Returns a list of the segments defined by the partition. Each segments holds its boundaries and a linear function.
        
    get_y(point: List)
        given a query point, finds the corresponding segment and returns the label obtained for the query point 
        by the linear function defined  in the segment.
        If the query point is not part of the space, the function returns None. 
"""

@dataclass
class MetaData:
    _d: int
    _segments: List[Segment]
    _type: Type = Type.CONTINUOUS
    _noise: int = 0

    @property
    def d(self):
        return self._d

    @property
    def segments(self):
        return self._segments

    def get_y(self, point: List):
        if len(point) != self._d:
            raise ValueError("A point must have the same dimensions as its dimensions")
        for segment in self._segments:
            y = segment.get_y(point)
            if y:
                return y
        return None
