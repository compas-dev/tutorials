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