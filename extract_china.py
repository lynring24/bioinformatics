import pandas as pd 
from Bio import SeqIO

df_covid = pd.read_csv('covid19.csv')
accessions = df_covid[df_covid.Geo_Location.str.contains('China', regex= True, na=False)]['Accession'].to_list()

# with open('china.txt', 'w') as file:
#     for access in accessions:
#        file.write("%s \n"%access)
     
seqs = SeqIO.parse("covid19.fasta", "fasta")

records = []
for seq in seqs:
        if seq.id[:-2] in accessions:
            print (seq.id)
            records.append(seq)
	
with open('covid19_china.fasta', 'w') as file:
	SeqIO.write(records, file, 'fasta')	
