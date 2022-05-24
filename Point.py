from __future__ import annotations
from typing import List
import math
import random


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_x(self) -> float:
        """
        Returns the x coordinate of this Point.
        """
        return self.x

    def get_y(self) -> float:
        """
        Returns the y coordinate of this Point.
        """
        return self.y

    def minus(self, other: Point) -> Point:
        """
        Returns a Point with x coordinate equals to this Point's x coordinate minus other Point's x coordinate
        and with y coordinate equals to this Point's y coordinate minus other Point's y coordinate.
        """
        return Point(self.get_x() - other.get_x(), self.get_y() - other.get_y())

    def cross_product(self, other: Point) -> float:
        """
        Returns the cross product of this Point and other Point.
        """
        return self.get_x() * other.get_y() - (other.get_x() * self.get_y())

    def distance_to(self, other: Point) -> float:
        """
        Returns the distance between this Point and other Point.
        """
        return math.sqrt((other.get_x() - self.get_x())**2 + (other.get_y() - self.get_y())**2)

    def is_left_of(self, other: Point) -> bool:
        """
        Returns True if this Point is left of the other Point.
        So if this point's x value is smaller than or equal to the other point's x value.
        """
        if self.get_x() <= other.get_x():
            return True
        else:
            return False

    def is_beneath_of(self, other: Point) -> bool:
        """
        Returns True if this Point is beneath the other Point.
        So if this point's y value is smaller than or equal to the other point's y value.
        """
        if self.get_y() <= other.get_y():
            return True
        else:
            return False

    def calculate_angle(self, reference_point: Point, other: Point) -> float:
        """
        Calculates the angle counter clockwise from the line segment [self, reference_point]
        to the line segment [self, other].
        The result is in radians.
        """
        distance_to_reference_point = self.distance_to(reference_point)
        distance_to_other = self.distance_to(other)
        if self.__eq__(reference_point) or self.__eq__(other):
            return 2 * math.pi
        distance_between_reference_point_and_other = reference_point.distance_to(other)
        numerator = distance_to_reference_point**2 + distance_to_other**2 - distance_between_reference_point_and_other**2
        denominator = 2 * distance_to_reference_point * distance_to_other
        quotient = numerator / denominator

        # fix for numerical errors, because for acos(x), x has to between -1 and 1
        if quotient > 1 or quotient < -1:
            quotient = int(quotient)

        angle = math.acos(quotient)

        if self.is_left_of(reference_point):
            if self.is_beneath_of(other):
                return angle
            else:
                return 2 * math.pi - angle
        else:
            if self.is_beneath_of(other):
                return 2 * math.pi - angle
            else:
                return angle

    def turns_left(self, previous_point: Point, next_point: Point) -> bool:
        """
        Returns True if you have to make a left turn going from line segment [previous_point, self] to
        the line segment [self, next_point] otherwise return False.
        """
        vector_one = next_point.minus(previous_point)
        vector_two = self.minus(previous_point)
        cross_product = vector_one.cross_product(vector_two)
        if cross_product < 0:
            return True
        else:
            return False

    @staticmethod
    def generate_random_point_point_list(number_of_points: int, max_coordinate: float, min_coordinate: float) -> list[Point]:
        """
        This method generates a list of n random Points, with n equals number_of_points.
        The x and y value of these points is randomly chosen between the given max_coordinate and min_coordinate.
        """
        result = list()
        for i in range(number_of_points):
            x_coordinate = random.uniform(min_coordinate, max_coordinate)
            y_coordinate = random.uniform(min_coordinate, max_coordinate)
            result.append(Point(x_coordinate, y_coordinate))
        return result

    def __str__(self):
        return "Point({}, {})".format(self.get_x(), self.get_y())

    def __repr__(self):
        return "Point({}, {})".format(self.get_x(), self.get_y())

    def __eq__(self, other: Point):
        if not isinstance(other, Point):
            return False
        else:
            if self.get_x() == other.get_x() and self.get_y() == other.get_y():
                return True
            else:
                return False
