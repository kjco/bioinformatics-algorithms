# Programming solution for:
#   Construct the De Bruijn Graph of a Collection of k-mers
#   http://rosalind.info/problems/ba3e/
#
# Given an arbitrary collection of k-mers Patterns (where some k-mers may
# appear multiple times), we define CompositionGraph(Patterns) as a graph with
# |Patterns| isolated edges. Every edge is labeled by a k-mer from Patterns,
# and the starting and ending nodes of an edge are labeled by the prefix and
# suffix of the k-mer labeling that edge. We then define the de Bruijn graph of
# Patterns, denoted DeBruijn(Patterns), by gluing identically labeled nodes in
# CompositionGraph(Patterns), which yields the following algorithm.
#
# **De Bruijn Graph from k-mers Problem**
# 
# Construct the de Bruijn graph from a collection of k-mers.
#   - Given: A collection of k-mers Patterns.
#   - Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency
#     list.

# Sample input: 
# pattern_list = ['GAGG','GGGG','GGGA','CAGG','AGGG','GGAG']
pattern_list = [line.strip() for line in open('dataset_54_7.txt','r')]
d = dict()

for kmer in pattern_list:
    prefix = kmer[0:len(kmer)-1]
    suffix = kmer[1:len(kmer)]
    if prefix not in d:
        d[prefix] = [suffix]
    else:
        d[prefix].append(suffix)
        
for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, ','.join(sorted(list(set(d[key])))))

# list(set(my_list)) removes duplicates in list
