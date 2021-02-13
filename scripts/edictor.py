from lingpy import *

## Creating a worldlist for Edictor
#wl = Wordlist.from_cldf('cldf/cldf-metadata.json')
#wl.add_entries('cogid', 'tokens', lambda x: 0)
#wl.add_entries('cogids', 'tokens', lambda x: 0)
#wl.add_entries('morphemes', 'tokens', lambda x: '?')
#wl.output('tsv', filename='wordlist')

wl = Wordlist('wordlist.tsv')

from lingpy.convert.strings import write_nexus
nexus = write_nexus(wl, ref='ALIGNMENT', mode='beast', filename='chibcu2.nex')
