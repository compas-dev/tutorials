import pathlib
from compas.geometry import Frame, Box, Cylinder

R = 1.4
YZ = Frame.worldYZ()
ZX = Frame.worldZX()
XY = Frame.worldXY()

box = Box(2 * R).to_brep()

cx = Cylinder(0.7 * R, 4 * R, frame=YZ).to_brep()
cy = Cylinder(0.7 * R, 4 * R, frame=ZX).to_brep()
cz = Cylinder(0.7 * R, 4 * R, frame=XY).to_brep()

result = box - (cx + cy + cz)

here = pathlib.Path(__file__).parent
result.to_step(here / "booleans.stp")
