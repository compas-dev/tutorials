# Use COMPAS with FastAPI

This tutorial gives an example how to run COMPAS as web service, which can be deployed on anywhere such as your local computer of a remote server on cloud platforms. To do this, besides COMPAS, we also use a popular web framework [FastAPI](https://fastapi.tiangolo.com/).

## Setup

Create a new environment with COMPAS installed.
```bash
conda create -n compas-server compas -y
```

Activate the environment we just created.
```bash
conda activate compas-server
```

We then install server-related utilities.
```bash
pip install fastapi uvicorn  pydantic
```

## Create a simple web server

We create a simple web server with FastAPI, called `server.py`. The server will have a single endpoint `/` which returns a greeting message.

```python
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return "Hello, this is a simple COMPAS server."


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

We can now start the server by running:
```bash
python server.py
```
```
INFO:     Started server process [45688]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

We can now visit the endpoint using `curl`:
```bash
curl http://localhost:8000
```
```
"Hello, this is a simple COMPAS server."
```

Alternatively, we can also using a simple python client.
```python
import requests

response = requests.get("http://localhost:8000")
print(response.text)
```
```
"Hello, this is a simple COMPAS server."
```

## Add an COMPAS endpoint to compute something.

We can now add an endpoint to compute something using COMPAS. For example, we can compute the orientated bounding box of a given list of points.

For this purpose, we use a function call `compas.geometry.oriented_bounding_box`. It takes a list of points as input and returns the vertices of the bounding box that is orientated by the principal axes of the points.


First, we define the input of the endpoint. FastAPI suggests to use [Pydantic](https://pydantic-docs.helpmanual.io/) for such purpose. In `server.py`, we add the following code to define the input of the endpoint.
```python
from pydantic import BaseModel
from typing import List


class OrientedBoundingBoxInput(BaseModel):
    points: List[List[float]]
```

We then add the endpoint to compute the bounding box.
```python
@app.post("/orinetated_bounding_box")
async def obb(orinetated_bounding_box_input: OrientedBoundingBoxInput):
    from compas.geometry import orinetated_bounding_box
    return orinetated_bounding_box(input.points)
```

Full code of `server.py` is as follows:
```python
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List
from compas.geometry import oriented_bounding_box

app = FastAPI()


class OrientedBoundingBoxInput(BaseModel):
    points: List[List[float]]


@app.get("/")
async def root():
    return "Hello, this is a simple COMPAS server."


@app.post("/oriented_bounding_box")
async def obb(oriented_bounding_box_input: OrientedBoundingBoxInput):
    return oriented_bounding_box(oriented_bounding_box_input.points)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

We can now start the server by running:
```bash
python server.py
```

We also update the python client to send a list of points to the server and print the vertices of the bounding box.
```python
response = requests.post("http://localhost:8000/orinetated_bounding_box", json={"points": [[0,0,0], [1,0,0], [0,1,0], [0,0,1]]})

print(response.json())
```
```
[[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.5, -0.5], [1.0, -0.5, 0.5], [-0.3333333333333333, -0.3333333333333333, 0.6666666666666667], [-0.3333333333333333, 0.6666666666666667, -0.33333333333333326], [0.6666666666666667, 0.1666666666666667, -0.8333333333333333], [0.6666666666666667, -0.8333333333333333, 0.16666666666666674]]
```