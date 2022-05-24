from Classes.Point import Point
from drawing import drawing
import grahams_scan


if __name__ == "__main__":
    point_list = Point.generate_random_point_list(100, 0, 2)
    convex_hull = grahams_scan.calculate_convex_hull(point_list, draw=True)
    drawing.show()
