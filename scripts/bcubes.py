from lingpy import *
from lingpy.evaluate.acd import bcubes, diff

lex = LexStat.from_cldf('../cldf/cldf-metadata.json', columns = [
    "concept_concepticon_id",
    "concept_name",
    "language_id",
    "language_name",
    "value", "form", "segments", "language_glottocode", 
    "cogid_cognateset_id"
    ])


lex.get_scorer(runs=10000)
lex.cluster(method='lexstat', threshold=0.55, cluster_method="upgma",
        ref="lexstatid")
lex.cluster(method='sca', threshold=0.45, cluster_method="upgma",
        ref="scaid")

diff(lex, 'cogid', 'lexstatid', filename="evaluate", pprint=False)
bcubes(lex, 'cogid', 'scaid')
bcubes(lex, 'cogid', 'lexstatid')


