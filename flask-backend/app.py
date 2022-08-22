from flask import Flask
from flask_restful import Api
from api import NERAPI, LanguagesAPI, ModelsAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(NERAPI, '/ner')
api.add_resource(LanguagesAPI, '/languages')
api.add_resource(ModelsAPI, '/models')

if __name__ == '__main__':
    app.run()
