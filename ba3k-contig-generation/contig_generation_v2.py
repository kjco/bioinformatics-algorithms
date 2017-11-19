# Programming solution for:
#   Generate Contigs from a Collection of Reads
#   http://rosalind.info/problems/ba3k/
#
# Even after read breaking, most assemblies still have gaps in k-mer coverage,
# causing the de Bruijn graph to have missing edges, and so the search for an
# Eulerian path fails. In this case, biologists often settle on assembling
# contigs (long, contiguous segments of the genome) rather than entire
# chromosomes. For example, a typical bacterial sequencing project may result
# in about a hundred contigs, ranging in length from a few thousand to a few
# hundred thousand nucleotides. For most genomes, the order of these contigs
# along the genome remains unknown. Needless to say, biologists would prefer to
# have the entire genomic sequence, but the cost of ordering the contigs into a
# final assembly and closing the gaps using more expensive experimental methods
# is often prohibitive.
# 
# Fortunately, we can derive contigs from the de Bruijn graph. A path in a graph
# is called non-branching if in(v) = out(v) = 1 for each intermediate node v of
# this path, i.e., for each node except possibly the starting and ending node of
# a path. A maximal non-branching path is a non-branching path that cannot be
# extended into a longer non-branching path. We are interested in these paths
# because the strings of nucleotides that they spell out must be present in any
# assembly with a given k-mer composition. For this reason, contigs correspond to
# strings spelled by maximal non-branching paths in the de Bruijn graph.
# 
# **Contig Generation Problem**
# 
# Generate the contigs from a collection of reads (with imperfect coverage).
#   - Given: A collection of k-mers Patterns.
#   - Return: All contigs in DeBruijn(Patterns). (You may return the strings in any
#     order.)


# Sample input:
# pattern_list = ['ATG','ATG','TGT','TGG','CAT','GGA','GAT','AGA']


pattern_list = [line.strip() for line in open('dataset_59_5.txt','r')]

d = dict()

for kmer in pattern_list:
    prefix = kmer[0:len(kmer)-1]
    suffix = kmer[1:len(kmer)]
    if prefix not in d:
        d[prefix] = [suffix]
    else:
        d[prefix].append(suffix)

def out_degree(db_dict,input_node):
    if input_node not in db_dict:
        return 0
    else:
        return len(db_dict[input_node])

def in_degree(db_dict,input_node):
    in_d = dict()
    for k,v in db_dict.iteritems():
        for node in v:
            if node not in in_d:
                in_d[node] = 1
            elif node in in_d:
                in_d[node] += 1
    if input_node not in in_d:
        return 0
    else:
        return in_d[input_node]

def decide(db_dict):
    for k,v in db_dict.iteritems():
        if v:
            return True
    return False


social_nodes = []
for k,v in d.iteritems():
    if out_degree(d,k) > 1:
        social_nodes.append(k)

#print 'social nodes'
#print social_nodes

popular_nodes = []
for k,v in d.iteritems():
    if in_degree(d,k) > 1:
        popular_nodes.append(k)

#print 'popular nodes:'
#print popular_nodes

branching_nodes = social_nodes + popular_nodes
#print 'branching nodes:'
#print branching_nodes

zero_in_nodes = []
for k,v in d.iteritems():
    if in_degree(d,k) == 0:
        zero_in_nodes.append(k)

#print 'zero in nodes:'
#print zero_in_nodes

contig_list = []

# Keep a list of nodes which have outdegree > 1. This is what you'll
# use as a reference for the rest of the program. Once a path
# encounters a node in this list, you'll have to stop.
#popular_nodes = find_out_degree_greater_than_one(d)

# Generate all paths starting from a node with outdegree > 1.
while decide(d):
    for i in branching_nodes:
        while len(d[i]) > 0:
            k_node = i
            k_initial = i
            cycle = [k_initial]
            # TODO: walk a path
            while True:
                orig_k = k_node
                k_node = d[k_node][0]
                d[orig_k].remove(d[orig_k][0])
                cycle.append(k_node)
                if k_node in social_nodes:
                    contig_list.append(cycle)
                    break
                if k_node in popular_nodes:
                    contig_list.append(cycle)
                    break
                if out_degree(d,k_node) == 0:
                    contig_list.append(cycle)
                    break
            
    for n in zero_in_nodes:
        if out_degree(d,n) > 0:
            k_node = n
            k_initial = n
            cycle = [k_initial]
            while True:
                orig_k = k_node
                k_node = d[k_node][0]
                d[orig_k].remove(d[orig_k][0])
                cycle.append(k_node)
                if k_node in social_nodes:
                    contig_list.append(cycle)
                    break
                if k_node in popular_nodes:
                    contig_list.append(cycle)
                    break
                if out_degree(d,k_node) == 0:
                    contig_list.append(cycle)
                    break

# Find a nodes with zero indegrees, and use it as the starting
# point. Loop until no such nodes exists.
#while node=zero_indegrees(d):
#    cycle = []
    # TODO: Walk a path
#    contig_list.append(cycle)

# Verify that there is no edges in the graph. 
#assert not decide(d)

#print contig_list
contig_str_list = []

for contig in contig_list:
    contig_str = ''
    for n in range(len(contig)-1):
        contig_str = contig_str + contig[n][0]
    contig_str = contig_str + contig[len(contig)-1]
    contig_str_list.append(contig_str)

contig_str_list.sort()

print ' '.join(contig_str_list)
