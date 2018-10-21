from pathlib import Path


class Dirs:
    src = Path(__file__).parent
    analysis = src.parent / 'analysis'
    data = src.parent / 'data'
    items = src.parent / 'items'
    probes = src.parent / 'probes'


class ProbeStore:
    verbose = False


class Preprocess:
    OOV_SYMBOL = 'OOV'
    F_NOISE_SYMBOL = 'F_NOISE'
    P_NOISE_SYMBOL = 'P_NOISE'
    SPECIAL_SYMBOLS = [OOV_SYMBOL, F_NOISE_SYMBOL, P_NOISE_SYMBOL] + ['xxx', 'TITLED', 'NAME_B', 'NAME_I']
    pos2tags = {'verb': ['BES', 'HVS', 'MD', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
                'noun': ['NN', 'NNS', 'WP'],
                'adverb': ['EX', 'RB', 'RBR', 'RBS', 'WRB'],
                'pronoun': ['PRP'],
                'preposition': ['IN'],
                'conjunction': ['CC'],
                'interjection': ['UH'],
                'determiner': ['DT'],
                'particle': ['POS', 'RP', 'TO'],
                'punctuation': [',', ':', '.', "''", 'HYPH', 'LS', 'NFP'],
                'adjective': ['AFX', 'JJ', 'JJR', 'JJS', 'PDT', 'PRP$', 'WDT', 'WP$'],
                'special': []}


class Hub:
    random_seed = 0