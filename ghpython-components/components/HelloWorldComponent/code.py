"""
Hello World of Grasshopper Python components.

It returns a COMPAS point based on the x, y, z coordinates.

    Args:
        x: X value
        y: Y value
        z: Z value
    Returns:
        point: A COMPAS point.
"""

from ghpythonlib.componentbase import executingcomponent as component
from compas.geometry import Point


class HelloWorldComponent(component):
    def RunScript(self, x, y, z):
        self.Message = "Hello World!"
        x = x or 0
        y = y or 0
        z = z or 0

        return Point(x, y, z)
