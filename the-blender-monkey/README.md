# The Blender Monkey

Many geometry processing libraries and CAD software have recognizable sample data. For example, the computer graphics community has the Stanford Bunny, Rhino has the Rhinoceros head, and Blender has the Suzanne monkey. This tutorial shows how to load the Blender monkey into COMPAS data and move it to Rhino.

## Installation

In this tutorial, we will use COMPAS in three different environments and exchange data between them.
Before we can do that, we have to install COMPAS in these environments.

There are installation instructions available here:

* [COMPAS](https://compas.dev/compas/latest/userguide/installation.html)
* [Rhino 8](https://compas.dev/compas/latest/userguide/cad.rhino8.html)
* [Blender](https://compas.dev/compas/latest/userguide/cad.blender.html)

## Export the Monkey From Blender

The minimal version:

```python
import pathlib
import compas
from compas_blender.conversions import monkey_to_compas

monkey = monkey_to_compas().subdivided(k=2)

# replace "/path/to/some/folder"
# with the path to the folder where you want to save the mesh
filepath = pathlib.Path('/path/to/some/folder') / "monkey.json"
compas.json_dump(monkey, filepath)

```

### Create a Monkey Mesh in Blender

`compas_blender` has a convenience function for getting the Monkey mesh directly.

```python
from compas_blender.conversions import monkey_to_compas

monkey = monkey_to_compas()
```

If you print the type of the result you will see that it is an instance of `compas.datastructures.Mesh`.
This means you can, for example, futher subdivide the mesh (or use any other mesh function) before visualising or exporting it.
See the complete Mesh API here: <https://compas.dev/compas/latest/api/compas.datastructures.Mesh.html>.

```python
# the subdivided method doesn't modify the mesh in-place but returns a modified copy
monkey = monkey.subdivided(k=2)
```

### Visualize the mesh

This step is not needed for the export, but it is just nice to see what you have done so far.

```python
from compas.colors import Color
from compas.scene import Scene

sceen = Scene()
scene.clear()  # this gets rid of the default cube and camera
scene.add(monkey, color=Color.from_hex('#0092d2'))
scene.draw()
```

### Export to Mesh to a File

Note that in Blender all relative paths are relative to the current blend file.
Therefore you have to provide an absolute path to where you want to save the mesh.

```python
import pathlib

# replace "/path/to/some/folder"
# with the path to the folder where you want to save the mesh
filepath = pathlib.Path('/path/to/some/folder') / "monkey.json"

```

Then, use the COMPAS JSON exporter to dump the mesh in the file:

```python
import compas

compas.json_dump(monkey, filepath)
```

## Load the Mesh in Rhino

```python
import os  # you can use pathlib instead if you're working in CPython in Rhino 8
import compas
from compas.colors import Color
from compas.scene import Scene

filepath = os.path.join("/folder/where/you/saved/the/monkey", "monkey.json")

monkey = compas.json_load(filepath)

scene = Scene()
scene.clear()
scene.add(monkey, color=Color.pink())
scene.draw()
```
