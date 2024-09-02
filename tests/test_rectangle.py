import pytest
import source.shapes as shapes

"""
# Fixtures before moving it to the conftest file
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10,20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)
"""


"""
# Code logic without using fixture
def test_area():
    rectangle = shapes.Rectangle(10, 20)
    assert rectangle.area() == 10 * 20

def test_perimeter():
    rectangle = shapes.Rectangle(10, 20)
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)
"""

# Code logic WITH FIXTURE
def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle



