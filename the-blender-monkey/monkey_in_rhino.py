import os  # you could also use the pathlib if you're working in Rhino 8
from compas.colors import Color
from compas.datastructures import Mesh
from compas.scene import Scene

filepath = os.path.join(os.path.dirname(__file__), "monkey.json")
monkey = Mesh.from_json(filepath)

scene = Scene()
scene.clear()
scene.add(monkey, color=Color.from_hex("#0092d2"))
scene.draw()
