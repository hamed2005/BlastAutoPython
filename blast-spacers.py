import os
import re

from Bio.Blast import NCBIWWW
from Bio import SeqIO

spacersDir = "all-spacers-of-a-bacteria/"
blastResultDir = "blast-results/"

### How many files to process?
nb_bacteria = len([name for name in os.listdir(spacersDir)])
counter = 1

### Running through all bacteria spacers one by one
for fn in os.listdir(spacersDir):
	
	### Tracking progress	
	print "Bacteria %i of %i :\n" % (counter, nb_bacteria)
	counter += 1
	
	#input_file = open(spacersDir+fn, 'r')
	#record = SeqIO.read(spacersDir + fn, format = "fasta")
	
	### Parsing and fetching all spacers of a bacteria from multifasta file
	fasta_records = (r for r in SeqIO.parse(spacersDir + fn, "fasta"))
	
	### Running Blat using qblast() for each spacer
	for r in fasta_records:
		print "Blasting %s :\n" % (r.id)
		result_handle = NCBIWWW.qblast("blastn", "nt", r.seq)
		output_file = open(blastResultDir + r.id, 'w')
		
		output_file.write(result_handle.read())
		
		output_file.close()
		result_handle.close()
