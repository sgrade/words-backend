#!/usr/bin/env python3

import connexion

from swagger_server import encoder

from sys import path

'''
def main():
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Words'}, pythonic_params=True)
    # app.run(port=8080)
    app.run()
'''

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Words'}, pythonic_params=True)
    # app.run(port=8080)
    app.run()
