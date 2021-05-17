from typing import List
import Point
import drawing


def get_lowest_point(point_list: List[Point]) -> Point:
    """
    This method returns the lowest point in the points_list.
    """
    lowest_point = point_list[0]
    for point in point_list:
        if point.get_y() <= lowest_point.get_y():
            if point.get_y() == lowest_point.get_y() and point.get_x() < lowest_point.get_x():
                lowest_point = point
            else:
                lowest_point = point
    return lowest_point


def calculate_convex_hull(point_list: List[Point]) -> List[Point]:
    """
    This method returns a list of points which is in the right order such that, when these points are connected with
    their neighboring points in the list that it will be the convex hull of the given point_list.
    This method uses the Grahams scan method to calculate the convex hull.
    This method will also show the calculated convex hull using matplotlib.
    """
    if len(point_list) == 0:
        return []
    else:
        drawing.draw_dynamically(point_list, [], 0.1)
        lowest_point = get_lowest_point(point_list)
        reference_point = Point(lowest_point.get_x() + 1, lowest_point.get_y())
        sorted_point_list = sorted(point_list, key=lambda point: lowest_point.calculate_angle(reference_point, point))
        stack = [lowest_point] + sorted_point_list[:2]

        for i in range(2, len(sorted_point_list) - 1):
            current_point = sorted_point_list[i]

            while not stack[-1].turns_left(stack[-2], current_point):
                stack.pop()
                drawing.draw_dynamically(point_list, stack)

            stack.append(current_point)
            drawing.draw_dynamically(point_list, stack)

        stack.append(lowest_point)
        drawing.draw_set_of_points(point_list)
        drawing.draw_set_of_lines(stack)
        drawing.draw()
        return stack


