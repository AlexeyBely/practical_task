import logging
import math

from geometric import CalcShapes
from core.config import settings


logger = logging.getLogger(__name__)
        

def main():
    shapes = CalcShapes()
    aaa = shapes.calc_area(CalcShapes.Shapes.TRIANGLE, 3, 4, 5)
    print(f'{aaa}')


if __name__ == '__main__':
    main()
