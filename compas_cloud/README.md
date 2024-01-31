# Use COMPAS with compas_cloud

This tutorial shows how to run COMPAS as web service using websockets through [compas_cloud](). Different from RESTful API, websockets allow for a persistent connection between the client and the server, which is useful for applications that require real-time communication, such as interactive visualization. [compas_cloud]() is a COMPAS extension that simplifies the process of creating a websocket server.

## Setup

create a new environment with COMPAS installed.
```bash
conda create -n compas-server compas -y
```

Activate the environment we just created.
```bash
conda activate compas-server
```

Install compas_cloud.
```bash
pip install compas_cloud
```

## Start a COMPAS cloud server
The compas_cloud server can be started by a simple command:
```bash
python -m compas_cloud.server
```
```
starting compas_cloud server
Listenning at 127.0.0.1:9009
```

## Interact with the compas_cloud server using Python

The compas_cloud server can be reached through its URL using a websocket client, either locally or remotely. This is particularly useful when you want to run a computation on a powerful remote server, or when you need to use a python library that is not available in your current python environment, such as IronPython in Rhino and Revit.

For python, compas_cloud provides a client class called `Proxy`, that simplifies the process of interacting with the server. 

```python
>>> from compas_cloud import Proxy
>>> proxy = Proxy(host='127.0.0.1', port=9009)
```
```
connected to cloud using websockets client!
Reconnected to an existing server at 127.0.0.1:9009
```

The `Proxy` class provides a set of methods that can be used to interact with the server. For example, we can use the `Proxy` class to call a function on the server side, and get the result back.

```python
>>> from compas.geometry import Translation
>>> transform_points_numpy = proxy.function('compas.geometry.transform_points_numpy')
>>> T = Translation.from_vector([0, 0, 1])
>>> points = [[0,0,0], [1,0,0], [2,0,0], [3,0,0]]
>>> transform_points_numpy(points, T) # This calculation will be excuted on the server-side
```
```
[[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [2.0, 0.0, 1.0], [3.0, 0.0, 1.0]]
```

For iterative calculations, it might be more efficient to keep all objects on the server-side, without sending them back and forth between the client and the server. This can be done with the `cache`. Which will instruct the server to only send back a reference. Once all calculations are done, the client can use the `get` method to retrieve the object from the server.

```python
>>> transform_points_numpy = proxy.function('compas.geometry.transform_points_numpy', cache=True)
>>> T = translation_from_vector([0, 0, 1])
>>> T = proxy.cache(T) # This will send the translation object to the server and return a reference
>>> T
```
```
{'cached': 140599247180896}
```
```python
>>> points = [[0,0,0], [1,0,0], [2,0,0], [3,0,0]]
>>> for i in range(5):
        points = transform_points_numpy(points, T) # The result will be returned as a reference
>>> points
```
```
{'cached': 140599265964944}
```
```python
>>> proxy.get(points) # This will retrieve the object from the server
```
```
[[0.0, 0.0, 5.0], [1.0, 0.0, 5.0], [2.0, 0.0, 5.0], [3.0, 0.0, 5.0]]
```
For examples please refer to the [compas_cloud documentation](https://compas.dev/compas_cloud).

## Interact with the compas_cloud server using JavaScript

Another common use case of compas_cloud is to use it as a backend for web applications. In this case, the client can be a web browser, or another server using different programming languages.

