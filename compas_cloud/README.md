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
You can find the full script at [client.py](client.py).
For more examples please refer to the [compas_cloud Repo](https://github.com/compas-dev/compas_cloud).

## Interact with the compas_cloud server using JavaScript

Another common use case of compas_cloud is to use it as a backend for web applications. In this case, the client can be a web browser, or another server using different programming languages.

For Javascript, we can use WebSocket API to connect to the compas_cloud server. The following example shows how to connect to the server and call a function on the server side. This example uses node.js, but it can also be used in a web browser in a very similar way. To run the example, first install the `ws` package.
```bash
npm install ws
```
This script is at [client.js](client.js).

```javascript
const WebSocket = require('ws');

class Client {

    constructor() {
        this.ws = new WebSocket('ws://localhost:9009');
        this.ws.on('error', console.error);
        this.ws.on('open', () => {
            console.log('connected');
        });
        this.ws.on('message', (data) => {
            console.log('received: %s', data);
            this.response = JSON.parse(String(data));
        });
    }

    run(packageName, args = [], kwargs = {}, cache = false) {
        this.response = null;
        let data = {
            package: packageName,
            args,
            kwargs,
            cache
        };
        this.ws.send(JSON.stringify(data));
    }

}

client = new Client();

setTimeout(() => {
    let points = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]];
    let matrix4 = [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 0.0, 1.0]];

    client.run('compas.geometry.transform_points', args = [points, matrix4]);

    setTimeout(() => {
        console.log(client.response);
        client.ws.close();
    }, 300);

}, 300);
```

Running the above script will print the following result:
```bash
node client.js
```
```
connected
received: [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [2.0, 0.0, 1.0], [3.0, 0.0, 1.0]]
[ [ 0, 0, 1 ], [ 1, 0, 1 ], [ 2, 0, 1 ], [ 3, 0, 1 ] ]
```

We can also use Javascript's Async/Await syntax to properly wait for connection and responses, rather than using `setTimeout` to wait for a fixed amount of time. The updated script is at [client_async.js](client_async.js).

```javascript
const WebSocket = require('ws');

class Client {

    constructor() {
        this.ws = null
    }

    async connect() {
        this.ws = new WebSocket('ws://localhost:9009');
        return new Promise((resolve, reject) => {
            this.ws.on('open', () => {
                console.log('connected');
                resolve();
            });
            this.ws.on('error', (err) => {
                reject(err);
            });
        });
    }

    async run(packageName, args = [], kwargs = {}, cache = false) {
        this.response = null;
        let data = {
            package: packageName,
            args,
            kwargs,
            cache
        };
        this.ws.send(JSON.stringify(data));

        this.ws.removeAllListeners('message');
        this.ws.removeAllListeners('error');

        return new Promise((resolve, reject) => {
            this.ws.on('message', (data) => {
                console.log('received: %s', data);
                this.response = JSON.parse(String(data));
                resolve(this.response);
            });

            this.ws.on('error', (err) => {
                reject(err);
            });
        });


    }

}

async function main() {
    let client = new Client();
    await client.connect();

    let points = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]];
    let matrix4 = [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 0.0, 1.0]];

    let response = await client.run('compas.geometry.transform_points', args = [points, matrix4]);
    console.log(response);

    client.ws.close()
}

main();
```