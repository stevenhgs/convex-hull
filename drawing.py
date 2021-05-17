from __future__ import annotations
from typing import List
import matplotlib.pyplot as plt
import Point


def draw_set_of_points(point_list: List[Point]) -> None:
    """
    This method draws the points in point_list using a red color.
    """
    for point in point_list:
        plt.plot(point.get_x(), point.get_y(), 'ro')


def draw_set_of_points_in_blue(point_list: List[Point]) -> None:
    """
    This method draws the points in point_list using a red color.
    """
    for point in point_list:
        plt.plot(point.get_x(), point.get_y(), 'bo')


def draw_set_of_lines(sequence_of_points: List[Point]) -> None:
    """
    This method draws lines between two neighboring points in sequence_of_points.
    """
    x_coordinate_list = list()
    y_coordinate_list = list()
    for point in sequence_of_points:
        x_coordinate_list.append(point.get_x())
        y_coordinate_list.append(point.get_y())
    plt.plot(x_coordinate_list, y_coordinate_list)


def show() -> None:
    plt.show()


def draw() -> None:
    plt.draw()


def draw_dynamically(point_list: List[Point], sequence_of_points: List[Point], pause=0.1) -> None:
    """
    This method is used to draw and show how grahams scan works.
    """
    draw_set_of_points(point_list)
    draw_set_of_lines(sequence_of_points)
    draw()
    plt.pause(pause)
    plt.clf()
