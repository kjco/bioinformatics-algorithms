# Programming solution for:
#   Find Substrings of a Genome Encoding a Given Amino Acid String
#   http://rosalind.info/problems/ba4b/
#
# There are three different ways to divide a DNA string into codons for
# translation, one starting at each of the first three starting positions of
# the string. These different ways of dividing a DNA string into codons are
# called reading frames. Since DNA is double-stranded, a genome has six reading
# frames (three on each strand), as shown in Figure 1.
# 
# We say that a DNA string Pattern encodes an amino acid string Peptide if the
# RNA string transcribed from either Pattern or its reverse complement Pattern
# translates into Peptide.
#
# **Peptide Encoding Problem**
#
# Find substrings of a genome encoding a given amino acid sequence.
#   - Given: A DNA string Text and an amino acid string Peptide.
#   - Return: All substrings of Text encoding Peptide (if any such substrings exist).

import string

codon_dict = {"AAA":"K","AAC":"N","AAG":"K","AAU":"N","ACA":"T","ACC":"T","ACG":"T","ACU":"T","AGA":"R","AGC":"S","AGG":"R","AGU":"S","AUA":"I","AUC":"I","AUG":"M","AUU":"I","CAA":"Q","CAC":"H","CAG":"Q","CAU":"H","CCA":"P","CCC":"P","CCG":"P","CCU":"P","CGA":"R","CGC":"R","CGG":"R","CGU":"R","CUA":"L","CUC":"L","CUG":"L","CUU":"L","GAA":"E","GAC":"D","GAG":"E","GAU":"D","GCA":"A","GCC":"A","GCG":"A","GCU":"A","GGA":"G","GGC":"G","GGG":"G","GGU":"G","GUA":"V","GUC":"V","GUG":"V","GUU":"V","UAA":"","UAC":"Y","UAG":"","UAU":"Y","UCA":"S","UCC":"S","UCG":"S","UCU":"S","UGA":"","UGC":"C","UGG":"W","UGU":"C","UUA":"L","UUC":"F","UUG":"L","UUU":"F"}
amino_acid_list = []

open_file = open('test_input.txt', 'r')
dna_string = open_file.readline().rstrip('\n')
open_file.close()
#dna_string = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
aa_seq = "KEVFEPHYY"
aa_seq_len = len(aa_seq)
rna_string = dna_string.replace('T','U')
rna_string_len = len(rna_string)
remainder = rna_string_len%3
#print rna_string_len
#print remainder
output_file = []

def comp(str):
    intab = 'ATCG'
    outtab = 'TAGC'
    mt = string.maketrans(intab,outtab)
    return str.translate(mt)


for i in range(3):
    amino_acid_list = []
    for j in range((rna_string_len/3)-i):
        codons = rna_string[3*j+i:3*j+3+i]
        amino_acid = codon_dict[codons]
        amino_acid_list.append(amino_acid)
        protein_string = str(''.join(amino_acid_list))
    #print protein_string
    for m in range(len(protein_string)-aa_seq_len):
        if aa_seq == protein_string[m:m+aa_seq_len]:
            output_file.append(dna_string[3*m+i:3*m+aa_seq_len*3+i])
            #output_file.append(m)

print output_file

reverse_seq = dna_string[::-1]
replace_seq = comp(reverse_seq)

#print replace_seq

rna_rev = replace_seq.replace('T','U')

#print rna_rev
rna_rev_len = len(rna_rev)
rev_output_file = []

for i in range(3):
    rev_amino_acid_list = []
    for j in range((rna_rev_len/3)-i):
        rev_codons = rna_rev[3*j+i:3*j+3+i]
        rev_amino_acid = codon_dict[rev_codons]
        rev_amino_acid_list.append(rev_amino_acid)
        rev_protein_string = str(''.join(rev_amino_acid_list))
    #print rev_protein_string
    for m in range(len(rev_protein_string)-aa_seq_len+1):
        if aa_seq == rev_protein_string[m:m+aa_seq_len]:
            rev_output_file.append(replace_seq[3*m+i:3*m+aa_seq_len*3+i]) 
            #rev_output_file.append(m)

#print rev_output_file

translated_output_file = []
for output_seq in rev_output_file:
   translated_output_file.append(comp(output_seq)[::-1])

print translated_output_file

all_output = output_file + translated_output_file

print all_output

print '\n'.join(all_output)


