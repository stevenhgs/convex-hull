from __future__ import annotations
from typing import Tuple, List
import math
import Point
import drawing


def get_lowest_and_highest_point(point_list: List[Point]) -> Tuple[Point, Point]:
    """
    This method returns the lowest point and the highest point in the points_list.
    """
    lowest_point = point_list[0]
    highest_point = point_list[0]
    for point in point_list:

        if point.get_y() <= lowest_point.get_y():
            if point.get_y() == lowest_point.get_y() and point.get_x() < lowest_point.get_x():
                lowest_point = point
            else:
                lowest_point = point

        if point.get_y() >= highest_point.get_y():
            if point.get_y() == highest_point.get_y() and point.get_x() > highest_point.get_x():
                highest_point = point
            else:
                highest_point = point

    return lowest_point, highest_point


def calculate_convex_hull(point_list: List[Point]) -> List[Point]:
    """
    This method returns a list of points which is in the right order such that, when these points are connected with
    their neighboring points in the list that it will be the convex hull of the given point_list.
    This method uses the Jarvis march method to calculate the convex hull.
    This method will also show the calculated convex hull using matplotlib.
    """
    if len(point_list) == 0:
        return []
    else:
        lowest_point, highest_point = get_lowest_and_highest_point(point_list)
        passed_highest_point = False
        current_point = lowest_point
        result = [current_point]
        while not (current_point == lowest_point and passed_highest_point):

            # constructing reference point
            if passed_highest_point:
                reference_point = Point.Point(current_point.get_x() - 1, current_point.get_y())
            else:
                reference_point = Point.Point(current_point.get_x() + 1, current_point.get_y())

            # getting point with smallest angle compared to current_point and reference_point
            smallest_angle = 2*math.pi
            point_with_smallest_angle = current_point
            for point in point_list:
                current_angle = current_point.calculate_angle(reference_point, point)
                if current_angle < smallest_angle:
                    smallest_angle = current_angle
                    point_with_smallest_angle = point

            current_point = point_with_smallest_angle
            result.append(current_point)

            # check if current_point is the highest point
            if current_point.__eq__(highest_point):
                passed_highest_point = True

        drawing.draw_set_of_points(point_list)
        drawing.draw_set_of_lines(result)
        drawing.draw()

        return result
