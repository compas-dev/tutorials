# COMPAS for Building Information Modelling

> **WARNING:** COMPAS IFC is currently being upgraded to support COMPAS 2.0.
> This upgrade is scheduled to be completed by the end of January 2024.
> This tutorial is the intended usage for COMPAS IFC with COMPAS 2.0.
> If you wish to use COMPAS IFC at its current state, please refer to the [COMPAS IFC documentation](https://compas.dev/compas_ifc).


## Setup

Create a new environment with BIM related packages in COMPAS ecosystem. Where `bim` is the name of the environment. `compas_ifc` is a package for reading and writing IFC files, a widely used digital format for BIM applications. `compas_viewer` is a package for creating custom viewers.
```bash
conda create -n bim compas_ifc compas_occ compas_viewer
```

Alternatively, you can create the environment from the provided `environment.yml` file.
```bash
conda env create -f environment.yml
```

Activate the environment and start the Python interpreter.
```bash
conda activate bim
python
```

Check the version installed packages.
```bash
>>> import compas_ifc
>>> compas_ifc.__version__
'1.0.0'
>>> import compas_viewer
>>> compas_ifc.__version__
'2.0.1'
```

## Load an IFC file
Load an IFC file into a `IFCModel` object. And print a summary of the model.
```bash
>>> from compas_ifc import IFCModel
>>> model = IFCModel.from_file('data/wall-with-opening-and-window.ifc')
>>> model.summary()
===============================================================================
IFCModel summary
-------------------------------------------------------------------------------
Filename: data/wall-with-opening-and-window.ifc
File size: 0.5 MB
Entity count: 123
Project: "Wall with opening and window"
Buildings: 1
...
===============================================================================
```
Print the spatial hierrachy of the model.
```
>>> model.print_hierarchy()
└── Default Project [IfcProject]
    └── Default Site [IfcSite]
        └── Default Building [IfcBuilding]
            └── Default Building Storey [IfcBuildingStorey]
                ├── Wall [IfcWall]
                │   └── Wall Openning [IfcOpeningElement]
                └── Window [IfcWindow]
```
Visualize the model in a viewer.
```
>>> model.show()
```
Full script at [1.load_ifc.py](scripts/1.load_ifc.py).

## Inspect entities in the Model

Get entities by type:
```
>>> walls = model.get_entities_by_type('IfcWall')
>>> walls
[<#5 IfcWall>]
>>> windows = model.get_entities_by_type('IfcWindow')
>>> windows
[<#7 IfcWindow>] 
``` 

Get entities through object attributes:
```
>>> walls = model.project.buildings[0].building_storeys[0].walls
>>> walls
[<#5 IfcWall>]
```

Show attributes of an entity
```
>>> wall = walls[0]
>>> wall.print_attributes(max_depth=3)
...
```

Show property sets of an entity
```
>>> wall.print_property_sets()
...
```

Access Geometry representations of an entity
```
>>> wall.representations
{"body": <compas.datastructures.Mesh>, "axis": <compas.datastructures.Polyline>}
>>> wall.representations['body']
...
>>> wall.representations['axis']
...
```

Full script at [2.inspect_entities.py](scripts/2.inspect_entities.py).

## Export selected entities
...

Full script at [3.export_entities.py](scripts/3.export_entities.py).

## Create new IFC file from scratch
...

Full script at [4.create_ifc.py](scripts/4.create_ifc.py).

