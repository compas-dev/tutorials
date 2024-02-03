from pathlib import Path
from compas_blender.conversions import monkey_to_compas
from compas.colors import Color
from compas.scene import Scene

# get the Suzanne monkey from Blender
# and subdivide the mesh using catmull-clark
monkey = monkey_to_compas().subdivided(k=2)

# optional:
# create a scene
# and visualize the monkey
scene = Scene()
scene.clear()
scene.add(monkey, color=Color.from_hex("#0092d2"))
scene.draw()

# export the monkey to a json file
# which we will load in Rhino
# note: you have to use an absolute path here,
#       because paths in Blender are relative to the blend file
filepath = Path("~/Code/tutorials/the-blender-monkey/monkey.json").expanduser()
monkey.to_json(filepath)
