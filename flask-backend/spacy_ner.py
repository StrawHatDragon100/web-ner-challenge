from flask_restful import Resource


class SpacyNER(Resource):
    def __init__(self, model):
        self.model = model

    def process(self, text):
        ner_results = self.model(text)
        if len(ner_results.ents) == 0:
            return 'No entities found.'
        done_entities = set()
        entities = set()
        for entity in ner_results.ents:
            if entity.text not in done_entities:
                done_entities.add(entity.text)
                entities.add(entity)
        for entity in set(entities):
            text = text.replace(entity.text, f'[{entity.text}:{entity.label_}]')
        return text

