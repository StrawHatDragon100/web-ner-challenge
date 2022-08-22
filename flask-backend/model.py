import spacy

SPACY_MODEL_SLUGS = {
    'en_core_web_sm': 'Small',
    'en_core_web_trf': 'Transformer',
    'fr_core_news_sm': 'Small',
    'fr_dep_news_trf': 'Transformer'
}

SPACY_MODELS = {
    'english': {
        'en_core_web_sm': spacy.load('en_core_web_sm'),
        'en_core_web_trf': spacy.load('en_core_web_trf'),
    },
    'french': {
        'fr_core_news_sm': spacy.load('fr_core_news_sm'),
        'fr_dep_news_trf': spacy.load('fr_dep_news_trf')
    }
}

LANGUAGE_SLUGS = {
    'english': 'English',
    'french': 'French'
}


def get_language_models(language: str):
    return [{'slug': SPACY_MODEL_SLUGS[model], 'value': model} for model in SPACY_MODELS.get(language).keys()]


def get_languages():
    return [{'slug': LANGUAGE_SLUGS[language], 'value': language} for language in SPACY_MODELS.keys()]
