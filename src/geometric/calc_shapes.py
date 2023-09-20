import math
from enum import Enum


class CalcShapes:
    """Calculating area geametrical shape."""
    
    class Shapes(Enum):
        CIRCLE = 'circle'
        RECTANGLE = 'rectangle'
        TRIANGLE = 'triangle'

    def calc_area(self, shape: Shapes, *args) -> float | None:
        """Calculating the area of the selected figure.
        
        If the result is None, the shape parameters are set incorrectly.
        """
        return self._shapes_map(shape, *args)    

    def circle_area(self, radius: float) -> float:
        """Calculating circle area."""
        return math.pi * radius * radius
    
    def rectangle_area(self, length: float, width: float) -> float | None:
        """Calculating rectangle area."""
        area = length * width
        if area < 0:
            return None
        return length * width
    
    def triangle_area(self, a: float, b: float, c: float) -> float | None:
        """Calculating triangle area."""
        edges = [a, b, c]
        edges.sort()
        if math.pow(edges[0], 2) + math.pow(edges[1], 2) == math.pow(edges[2], 2):
            return edges[0] * edges[1] / 2
        p = (a + b + c) / 2
        check_num = p * (p - a) * (p - b) * (p - c)
        if check_num < 0:
            return None
        return math.pow(check_num, 0.5)

    def _shapes_map(self, shape: Shapes, *args):
        map_ = {
            'circle': self.circle_area,
            'rectangle': self.rectangle_area,
            'triangle': self.triangle_area,
        }
        return map_[shape.value](*args) 
