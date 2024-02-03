# Create Grasshopper Python components

This tutorial provides an example of how to create Grasshopper components using Python. This allows components to be version controlled.

## Setup

Install IronPython 2.7.8 using Chocolatey or using the installer from the [IronPython website](https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.8/).


## Create a simple Grasshopper component

Each new component needs to be in its own folder. We're going to name our first component `HelloWorldComponent`, and create a folder for it inside the `components` folder.

Inside the component folder, we need three files: a code file (`code.py`), an icon file (`icon.png`) and a JSON metadata file (`metadata.json`).

The code file contains the script that you want to run in our component. The following simple example creates a component that prints "Hello, world!" in the component's message box and returns a COMPAS point based on input parameters:

```python
from ghpythonlib.componentbase import executingcomponent as component
from compas.geometry import Point


class HelloWorldComponent(component):
    def RunScript(self, x, y, z):
        self.Message = "Hello World!"
        x = x or 0
        y = y or 0
        z = z or 0

        return Point(x, y, z)
```

The JSON metadata file defines inputs and outputs for our component, and a few additional options. For our component we can use the following file:

```json
{
    "name": "Hello World component",
    "nickname": "HelloWorld",
    "description": "Hello world of Grasshopper python components!",
    "category": "Tutorials",
    "subcategory": "Hello",

    "ghpython": {
        "isAdvancedMode": true,
        "inputParameters": [
            {
                "name": "x"
            },
            {
                "name": "y"
            },
            {
                "name": "z"
            }
        ],
        "outputParameters": [
            {
                "name": "point"
            }
        ]
    }
}
```

The icon file can be any PNG image of `24x24` pixels.

Once we have our files, we can compile our component using IronPython:

```bash
ipy componentizer\componentize.py components output
```

After running this, we will find our component in the `output` folder, ready to be used! Just drag into into the Grasshopper canvas and start using it! 🚀

![Grasshopper component](components.png)