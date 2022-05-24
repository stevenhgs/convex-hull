from Classes.Point import Point
from drawing import drawing
import jarvis_march

point_list = Point.generate_random_point_list(25, 0, 2)
convex_hull = jarvis_march.calculate_convex_hull(point_list)
drawing.show()
