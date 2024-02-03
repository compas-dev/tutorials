# Brep Booleans in VS Code

COMPAS has a geometry processing library that can be used independent of CAD software. In this tutorial we apply boolean operations to a Brep, direclty in VS Code, and visualise the result using a Jupyter notebook viewer.

## Clone the Tutorial(s)

Before you start, clone the `compas.dev/tutorials.git` repo to your computer.

```bash
git clone https://compas.dev/tutorials.git
cd tutorials/brep-booleans-vscode
```

## Installation

```bash
conda env create -f environment.yml
```

## Activate the environment in VS Code

To activate the envinronment in VS Code, do <kbd>SHIFT</kbd> + <kbd>Cmd</kbd> + <kbd>P</kbd> (OSX) or <kbd>SHIFT</kbd> + <kbd>Ctrl</kbd> + <kbd>P</kbd> (Windows) and type "Python: Select Interpreter" in the Command Palette. Then choose `compas-tutorials` from the list of environments.

## Boolean Operations + Visualisation

To do everything in one go (boolean operations + visualisation), open `brep-booleans.ipynb` , choose the current environment as kernel, and run all cells.

Alternatively, you can generate the booleans in a normal script first, export the data, and use a notebook just for the visulisation part.

## Just the Booleans

In the future, Breps can be serialised to JSON like all other COMPAS objects.
However, this is currently not available yet.
For now, you can instead convert the Brep to a STEP file.

```python
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
result.to_step(here / 'booleans.stp')

```

## Just the Visualization

If you have saved the result as a STEP file, we can load that in the notebook viewer to visualize the result.
Just open `brep-booleans_viz-only.ipynb` , choose the current environment as kernel (if necessary), and run all cells.

IMPORTANT: due to a small bug (which will be fixed soon), you have to close the other notebooks for the viewer to work properly...
