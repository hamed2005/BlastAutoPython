import os
import re

from Bio.Blast import NCBIWWW
from Bio import SeqIO

blastResultDir = "blast-results/"

### Parsing and fetching all spacers from all-spacers.fasta
fasta_records = (r for r in SeqIO.parse("all-spacers.fasta", "fasta"))
	
### Running Blast for each spacer
for r in fasta_records:
	### Tracking progress
	print "Blasting %s :\n" % (r.id)
	result_handle = NCBIWWW.qblast("blastn", "nt", r.seq, expect = 0.001, megablast = "FALSE", filter = None, format_type = "Text", ncbi_gi = True, entrez_query = '(2157[taxid] OR 2[taxid] OR 10239[taxid])')
	output_file = open(blastResultDir + r.id, 'w')
	
	output_file.write(result_handle.read())
	
	output_file.close()
	result_handle.close()
