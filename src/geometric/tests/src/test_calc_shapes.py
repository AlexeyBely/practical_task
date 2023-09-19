

def test_circle_area(shapes):
    type_shapes = shapes.Shapes.CIRCLE

    assert round(shapes.calc_area(type_shapes, 5), 8) == 78.53981634
    assert round(shapes.calc_area(type_shapes, 1), 8) == 3.14159265


def test_rectangle_area(shapes):
    type_shapes = shapes.Shapes.RECTANGLE

    assert round(shapes.calc_area(type_shapes, 5.5, 4.3), 8) == 23.65
    assert shapes.calc_area(type_shapes, 10, 10) == 100
    assert shapes.calc_area(type_shapes, 10, -10) is None


def test_triangle_area(shapes):
    type_shapes = shapes.Shapes.TRIANGLE

    assert shapes.calc_area(type_shapes, 3, 4, 5) == 6
    assert round(shapes.calc_area(type_shapes, 1000, 1005, 10), 8) == 4340.89834453
    assert shapes.calc_area(type_shapes, 100, 110, 5) is None
