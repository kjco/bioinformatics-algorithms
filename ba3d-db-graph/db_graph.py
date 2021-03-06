# Programming solution for:
#   Construct the De Bruijn Graph of a String 
#   http://rosalind.info/problems/ba3d/
#
# Given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k +
# 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in
# Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in
# Text. The de Bruijn graph DeBruijnk(Text) is formed by gluing identically
# labeled nodes in PathGraphk(Text).
# 
# **De Bruijn Graph from a String Problem**
# 
# Construct the de Bruijn graph of a string.
#   - Given: An integer k and a string Text.
#   - Return:DeBruijnk(Text), in the form of an adjacency list.

def comp_string(text,k):
    comp_list = []
    for i in range(len(text)-k+1):
        comp = text[i:i+k]
        comp_list.append(comp)
    lex_comp_list = sorted(comp_list)
    return lex_comp_list

# Sample test input:
# input_text = 'AAGATTCTCTAC'
# input_k = 4
with open('dataset_53_6.txt','r') as f:
    input_k = int(f.readline().rstrip('\n'))
    input_text = f.readline().rstrip('\n')

kmer_list = comp_string(input_text,input_k-1)
d = dict()

for kmer in kmer_list:
    v_list = []
    for alt in kmer_list:
        if kmer[1:len(kmer)] == alt[0:len(alt)-1]:
            v_list.append(alt)
            d[kmer] = v_list


for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, ','.join(sorted(list(set(d[key])))))

# list(set(my_list)) removes duplicates in list
