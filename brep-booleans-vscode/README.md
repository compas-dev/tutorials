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

## Run the Jupyter Notebook

