from lingpy import *

wl = Wordlist.from_cldf('cldf/cldf-metadata.json')
wl.add_entries('cogid', 'tokens', lambda x: 0)
wl.add_entries('cogids', 'tokens', lambda x: 0)
wl.add_entries('morphemes', 'tokens', lambda x: '?')
wl.output('tsv', filename='wordlist')