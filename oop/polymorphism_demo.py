# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method to calculate the area. Should be overridden by derived classes."""
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor to initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the rectangle's area."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Constructor to initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the circle's area."""
        return math.pi * self.radius ** 2
