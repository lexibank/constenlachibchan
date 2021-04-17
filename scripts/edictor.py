from lexibank_constenlachibchan import Dataset
from lingpy import *
from lingpy.compare.partial import *
from lingpy.convert.strings import write_nexus
import io
from lingpy.convert.strings import matrix2dst


cols = ['concept_id', 'concept_name', 'language_id', 'language_name', 'value',
        'form', 'cogid', 'cogids', 'morphemes', 'segments', 'glottocode', 'concept_concepticon_id',
        'comment']


DS = Dataset()
lex = Partial.from_cldf(DS.cldf_dir.joinpath('../cldf/cldf-metadata.json'),
        columns=cols)

lex.partial_cluster(method='sca', threshold=0.45, ref="cogids")
alms = Alignments(lex, ref="cogid")
alms.align()

alms.add_entries('morphemes', 'tokens', lambda x: "")

at = ['Atanque'] 
alms.output('tsv', 
                filename='./AutoCognates/wordlist',
                subset=True,
                rows=dict(doculect = 'not in' +str(at)))
alms = Wordlist('./AutoCognates/wordlist.tsv')


nexus = write_nexus(alms,
       ref="COGID", 
       mode="beast", 
       filename='./AutoCognates/chibchan-beast_cu.nex')

dst = matrix2dst(alms.get_distances(ref='COGID', mode='swadesh'), alms.taxa)


with io.open('./AutoCognates/chibchan_cu.dst', 'w', encoding='utf8') as fp:
    fp.write(dst)
