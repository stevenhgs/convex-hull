from Classes.Point import Point
from drawing import drawing
import jarvis_march


if __name__ == "__main__":
    point_list = Point.generate_random_point_list(25, 0, 2)
    convex_hull = jarvis_march.calculate_convex_hull(point_list, draw=True)
    drawing.show()
