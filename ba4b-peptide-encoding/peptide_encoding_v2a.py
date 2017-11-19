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

codon_dict = {"AAA":"K","AAC":"N","AAG":"K","AAU":"N","ACA":"T","ACC":"T","ACG":"T","ACU":"T","AGA":"R","AGC":"S","AGG":"R","AGU":"S","AUA":"I","AUC":"I","AUG":"M","AUU":"I","CAA":"Q","CAC":"H","CAG":"Q","CAU":"H","CCA":"P","CCC":"P","CCG":"P","CCU":"P","CGA":"R","CGC":"R","CGG":"R","CGU":"R","CUA":"L","CUC":"L","CUG":"L","CUU":"L","GAA":"E","GAC":"D","GAG":"E","GAU":"D","GCA":"A","GCC":"A","GCG":"A","GCU":"A","GGA":"G","GGC":"G","GGG":"G","GGU":"G","GUA":"V","GUC":"V","GUG":"V","GUU":"V","UAA":"-","UAC":"Y","UAG":"-","UAU":"Y","UCA":"S","UCC":"S","UCG":"S","UCU":"S","UGA":"-","UGC":"C","UGG":"W","UGU":"C","UUA":"L","UUC":"F","UUG":"L","UUU":"F"}
amino_acid_list = []

open_file = open('dataset_18_6.txt', 'r')
#open_file = open('test_input.txt', 'r')
dna_string = open_file.readline().rstrip('\n').rstrip('\r')
open_file.close()
#dna_string = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
aa_seq = "LWEEQAWH"
aa_seq_len = len(aa_seq)
rna_string = dna_string.replace('T','U')
rna_string_len = len(rna_string)
remainder = rna_string_len%3
#print rna_string_len
#print remainder

def comp(str):
    intab = 'ATCG'
    outtab = 'TAGC'
    mt = string.maketrans(intab,outtab)
    return str.translate(mt)

def find_matches(dna_seq):
    rna_seq = dna_seq.replace('T','U')

    match_list = []
    for i in range(3):
        amino_acid_list = []
        # Translating the rna seq into a protein sequence.
        #print len(rna_seq)-3-i
        for j in range(i, len(rna_seq)-3-i+1, 3):
            #print j
            codons = rna_seq[j:j+3]
            amino_acid = codon_dict[codons]
            #print codons, amino_acid
            amino_acid_list.append(amino_acid)
        protein_seq = str(''.join(amino_acid_list))
        #print protein_seq, len(protein_seq)

        # Find matches in the protein sequence.
        for m in range(len(protein_seq)-aa_seq_len+1):
            if aa_seq == protein_seq[m:m+aa_seq_len]:
                #print m
                match_list.append(dna_seq[3*m+i:3*m+aa_seq_len*3+i])
    return match_list


#print 'Length of DNA sequence is %d. The sequence is %s' % (
#    len(dna_string), dna_string)

# Find matches in the DNA sequence
match_list = find_matches(dna_string)

# Find matches in the reversed, comped DNA sequence
reverse_dna_seq = dna_string[::-1]
comp_reversed_dna_seq = comp(reverse_dna_seq)
#print 'comped, reversed DNA sequence is %s' % comp_reversed_dna_seq
match_list2 = find_matches(comp_reversed_dna_seq)
#print match_list2

translated_match_list2 = []
for seq in match_list2:
   translated_match_list2.append(comp(seq)[::-1])

print '\n'.join(match_list + translated_match_list2)
