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

# Sample test input:
text = 'AAGATTCTCTAC'
input_k = 4
#with open('dataset_53_6.txt','r') as f:
#    input_k = int(f.readline().rstrip('\n'))
#    text = f.readline().rstrip('\n')

k = input_k - 1
d = dict()

for i in range(len(text)-k):
    prefix = text[i:i+k]
    suffix = text[i+1:i+k+1]
    if prefix not in d:
        d[prefix] = [suffix]
    else:
        d[prefix].append(suffix)
        
for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, ','.join(sorted(list(set(d[key])))))

# list(set(my_list)) removes duplicates in list
