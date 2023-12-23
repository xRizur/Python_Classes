import pytest
from rectangles import Rectangle
from points import Point

def test_rectangle_properties():
    rect = Rectangle(1, 1, 4, 4)
    assert rect.left == 1
    assert rect.bottom == 1
    assert rect.right == 4
    assert rect.top == 4
    assert rect.width == 3
    assert rect.height == 3
    
    assert rect.topleft == Point(1, 1)
    assert rect.bottomright == Point(4, 4)

def test_rectangle_center():
    rect = Rectangle(0, 0, 2, 2)
    assert rect.center == Point(1, 1)

def test_rectangle_from_points():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    rect = Rectangle.from_points((p1, p2))
    assert rect.width == 3
    assert rect.height == 4

def test_rectangle_intersection():
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(2, 2, 5, 5)
    intersection = rect1.intersection(rect2)
    assert intersection == Rectangle(2, 2, 4, 4)

def test_rectangle_no_intersection():
    rect1 = Rectangle(1, 1, 2, 2)
    rect2 = Rectangle(3, 3, 4, 4)
    intersection = rect1.intersection(rect2)
    assert intersection is None

def test_rectangle_cover():
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(2, 2, 5, 5)
    cover = rect1.cover(rect2)
    assert cover == Rectangle(1, 1, 5, 5)

def test_rectangle_make4():
    rect = Rectangle(0, 0, 4, 4)
    rect1, rect2, rect3, rect4 = rect.make4()
    assert rect1 == Rectangle(0, 0, 2, 2)
    assert rect2 == Rectangle(2, 0, 4, 2)
    assert rect3 == Rectangle(0, 2, 2, 4)
    assert rect4 == Rectangle(2, 2, 4, 4)

