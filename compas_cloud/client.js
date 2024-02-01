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

