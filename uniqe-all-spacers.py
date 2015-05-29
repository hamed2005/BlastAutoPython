import re
from collections import Counter

sequence_regex = re.compile('[(A|T|C|G)]+\n')
all_spacers = open("all-spacers.fasta", 'r')
all_spacers_uniq = open("all-spacers-uniq.fasta", 'w')
all_spacers = all_spacers.read()

### Obtain all spacers
spacers = re.findall(sequence_regex, all_spacers)

### Build a dictionary of all found spacers {spacer: occurance}
uniq_spacers = Counter(spacers)

counter = 1
for item in uniq_spacers:
	all_spacers_uniq.writelines(">spacer_%i\n%s" % (counter, item))
	counter += 1

all_spacers_uniq.close()
