from model import SPACY_MODELS
from spacy_ner import SpacyNER


class NERFactory:
    @classmethod
    def get_ner(cls, language_slug, model_slug):
        return SpacyNER(model=SPACY_MODELS.get(language_slug, dict()).get(model_slug))
