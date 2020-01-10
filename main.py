#!/usr/bin/env python3

import config

import connexion

from swagger_server import encoder

from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Words'}, pythonic_params=True)

# add CORS support
CORS(app.app)

if __name__ == '__main__':
    app.run()
