from __future__ import annotations
import matplotlib.pyplot as plt
from Classes.Point import Point


def draw_point(point: Point, color='red') -> None:
    plt.plot(point.get_x(), point.get_y(), 'o', color=color)


def draw_points(points: list[Point], color='red') -> None:
    """
    This method draws the given points using the given color.
    """
    for point in points:
        plt.plot(point.get_x(), point.get_y(), 'o', color=color)


def draw_lines(sequence_of_points: list[Point]) -> None:
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


def draw_points_and_lines(points: list[Point], sequence_of_points: list[Point]) -> None:
    """
    This method draws the given points using the given color.
    This method also draws lines between two neighboring points in sequence_of_points.
    """
    draw_points(points)
    draw_lines(sequence_of_points)
    draw()


def draw_dynamically_grahams_scan(points: list[Point], sequence_of_points: list[Point], pause=0.01) -> None:
    """
    This method is used to draw and show how grahams scan works.
    """
    draw_points_and_lines(points, sequence_of_points)
    plt.pause(pause)
    plt.clf()
