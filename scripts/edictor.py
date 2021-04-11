from lexibank_constenlachibchan import Dataset
from lingpy import *
from lingpy.compare.partial import *


cols = ['concept_id', 'concept_name', 'language_id', 'language_name', 'value',
        'form', 'cogid', 'cogids', 'morphemes', 'segments', 'glottocode', 'concept_concepticon_id',
        'comment']


DS = Dataset()
lex = Partial.from_cldf(DS.cldf_dir.joinpath('cldf-metadata.json'),
        columns=cols)

lex.partial_cluster(method='sca', threshold=0.45, ref="cogids")
alms = Alignments(lex, ref="cogid")
alms.align()

alms.add_entries('morphemes', 'tokens', lambda x: "")

alms.output('tsv', filename='./scripts/AutoCognates/wordlist')
alms = Wordlist('./scripts/AutoCognates/wordlist.tsv')

# nexus = write_nexus(wl,
#       ref="COGIDS", 
#       mode="beast", 
#       filename='./AutoCognates/chibchan-beast_cu.nex')

# dst = matrix2dst(wl.get_distances(ref='COGID', mode='swadesh'), wl.taxa)

# with io.open('./AutoCognates/chibchan_cu.dst', 'w', encoding='utf8') as fp:
#    fp.write(dst)