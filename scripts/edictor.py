import io
from lexibank_constenlachibchan import Dataset
from lingpy import *
from lingpy.compare.partial import *
from lingpy.convert.strings import write_nexus
from lingpy.convert.strings import matrix2dst


cols = ['concept_id', 'concept_name', 'language_id', 'language_name', 'value',
        'form', 'cogid', 'cogids', 'morphemes', 'segments', 'cognacy', 'glottocode', 'concept_concepticon_id',
        'comment']


DS = Dataset()
lex = Partial.from_cldf(DS.cldf_dir.joinpath('../cldf/cldf-metadata.json'),
        columns=cols)

lex.get_scorer(runs=10000)
lex.partial_cluster(method='lexstat', threshold=0.55, cluster_method="upgma",
        ref="cogids")
alms = Alignments(lex, ref="cogids")
alms.align()
alms.add_entries('morphemes', 'tokens', lambda x: "")

at = ['Atanque']        # Atanque only has three entries in v0.1 and is thus excluded from any phylolinguistic analysis due to poor coverage
alms.output('tsv', 
                filename='./wordlist',
                subset=True,
                rows=dict(doculect = 'not in' +str(at)))

# The following part is for creating different files for phylolinguistic inference
alms = Wordlist('./wordlist.tsv')

nexus_ls = write_nexus(alms,
        ref="cogids", 
        mode="beast", 
        filename='./phylo_files/chibchan-beast_ls.nex')

nexus_cu = write_nexus(alms,
        ref="cognacy", 
        mode="beast", 
        filename='./phylo_files/chibchan-beast_cu.nex')

dst = matrix2dst(alms.get_distances(ref='cognacy', mode='swadesh'), alms.taxa)

with io.open('./phylo_files/chibchan_cu.dst', 'w', encoding='utf8') as fp:
    fp.write(dst)

