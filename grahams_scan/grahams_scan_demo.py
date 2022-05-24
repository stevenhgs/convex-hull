from Classes.Point import Point
from drawing import drawing
import grahams_scan

point_list = Point.generate_random_point_list(25, 0, 2)
convex_hull = grahams_scan.calculate_convex_hull(point_list)
drawing.show()