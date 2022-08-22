from flask_restful import Resource, reqparse
from ner_factory import NERFactory
from model import get_language_models, get_languages


class NERAPI(Resource):
    ner_parser = reqparse.RequestParser()
    ner_parser.add_argument('text', type=str, required=True)
    ner_parser.add_argument('language', type=str, required=True)
    ner_parser.add_argument('model', type=str, required=True)

    def post(self):
        args = self.ner_parser.parse_args()
        model_slug = args.get('model')
        language_slug = args.get('language')
        text = args.get('text')
        result = NERFactory.get_ner(language_slug, model_slug).process(text)
        return {'result': result}


class LanguagesAPI(Resource):
    def get(self):
        return get_languages()


class ModelsAPI(Resource):
    model_parser = reqparse.RequestParser()
    model_parser.add_argument('language', required=True, type=str, location='args')

    def get(self):
        args = self.model_parser.parse_args()
        language = args['language']
        return get_language_models(language)
