from flask import Flask
from flask_restful import Resource, Api


class MSEuMaisMais(Resource):

    def get(self):
        return {'eu': 'mais mais'}

    def post(self):
        return 200


class HomeEuMaisMais(Resource):

    def get(self):
        return 'Bem-vindo ao Eu++!'


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(HomeEuMaisMais, '/')
    api.add_resource(MSEuMaisMais, '/ms_eu_mais_mais/')
    return app
