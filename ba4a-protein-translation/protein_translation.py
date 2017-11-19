# Protein translation: input RNA string, output amino acid string

codon_dict = {"AAA":"K","AAC":"N","AAG":"K","AAU":"N","ACA":"T","ACC":"T","ACG":"T","ACU":"T","AGA":"R","AGC":"S","AGG":"R","AGU":"S","AUA":"I","AUC":"I","AUG":"M","AUU":"I","CAA":"Q","CAC":"H","CAG":"Q","CAU":"H","CCA":"P","CCC":"P","CCG":"P","CCU":"P","CGA":"R","CGC":"R","CGG":"R","CGU":"R","CUA":"L","CUC":"L","CUG":"L","CUU":"L","GAA":"E","GAC":"D","GAG":"E","GAU":"D","GCA":"A","GCC":"A","GCG":"A","GCU":"A","GGA":"G","GGC":"G","GGG":"G","GGU":"G","GUA":"V","GUC":"V","GUG":"V","GUU":"V","UAA":"","UAC":"Y","UAG":"","UAU":"Y","UCA":"S","UCC":"S","UCG":"S","UCU":"S","UGA":"","UGC":"C","UGG":"W","UGU":"C","UUA":"L","UUC":"F","UUG":"L","UUU":"F"}
amino_acid_list = []

open_file = open('dataset_18_3.txt', 'r')
rna_string = open_file.readline().rstrip('\n')
open_file.close()

#rna_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
rna_string_len = len(rna_string)

for i in range(rna_string_len/3):
    codons = rna_string[3*i:3*i+3]
    amino_acid = codon_dict[codons]
    amino_acid_list.append(amino_acid)

print amino_acid_list
print ''.join(amino_acid_list)

    
