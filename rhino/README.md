# Introduction

# Installation Rhino 7 IronPython Editor

- **Step 1:** Anaconda Prompt commands: a) create a new conda environment named e.g. *compas-dev*, or any other name, and install compas, b) activate the environment, and c) install compas_rhino for Rhino 7:

    ```bash
    conda create -n compas-dev -c conda-forge compas
    conda activate compas-dev
    python -m compas_rhino.install -v 7.0
    ```

    ![Conda Environment](conda_environment.png)

- **Step 2:** Open Rhino 7 and in the command line type ```EditPythonScript```:

    ![edit_python_script](edit_python_script.png) 

- **Step 3:** Use the following code to test, if compas is installed correctly:

    ```python
    import compas
    print(compas.__version__)
    ```

    ![edit_python_script_version_check](edit_python_script_version_check.png)


# Installation - Rhino 8 CPython Editor

- **Step 1:** Anaconda Prompt commands: a) create a new conda environment named e.g. *compas-dev*, or any other name, and install compas, b) activate the environment, and c) install compas_rhino for Rhino 8:

    ```bash
    conda create -n compas-dev -c conda-forge compas python=3.9
    conda activate compas-dev¨
    directory_of_rhinocode -m pip install compas
    ```

The *directory_of_rhinocode* of Rhino 8 CPython in Windows and Mac OS:
**WINDOWS** C:/Users/my_user_name/.rhinocode/py39-rh8/python.exe
**MAC** ~/.rhinocode/py39-rh8/python3.9

- **Step 2:** Open Rhino8 ```ScriptEditor``` in the command line:

    ![script_editor](script_editor.png) 

- **Step 3:** Use the following code to test, if compas is installed correctly:

    ```python
    import compas
    print(compas.__version__)
    ```

    ![script_editor_version_check](script_editor_version_check.png)


## Load geometry

Load a mesh from a file and display it in Rhino.


```bash
import compas
from compas.datastructures import Mesh
from compas.scene import Scene

mesh = Mesh.from_obj(compas.get('tubemesh.obj'))

scene = Scene()
scene.add(mesh)
scene.draw()
```

![rhino8](rhino8.png)
