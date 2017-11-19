

pattern_list = ['ATG','ATG','TGT','TGG','CAT','GGA','GAT','AGA']

d = dict()

for kmer in pattern_list:
    prefix = kmer[0:len(kmer)-1]
    suffix = kmer[1:len(kmer)]
    if prefix not in d:
        d[prefix] = [suffix]
    else:
        d[prefix].append(suffix)
        

print d

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

print 'social nodes'
print social_nodes

popular_nodes = []
for k,v in d.iteritems():
    if in_degree(d,k) > 1:
        popular_nodes.append(k)

print 'popular nodes:'
print popular_nodes

zero_in_nodes = []
for k,v in d.iteritems():
    if in_degree(d,k) == 0:
        zero_in_nodes.append(k)

print 'zero in nodes'
print zero_in_nodes


contig_list = []

while decide(d):
    max_count = 0
    for k,v in d.iteritems():
        if len(d[k]) > max_count:
            max_out_degree = k
            max_count = len(d[k])

    k_node = max_out_degree
    k_initial = max_out_degree
    cycle = [k_initial]
    while True:
        orig_k = k_node
        k_node = d[k_node][0]
        d[orig_k].remove(d[orig_k][0])
        cycle.append(k_node)
        if out_degree(d,orig_k) > 1:
            contig_list.append(cycle)
            break
        if in_degree(d,orig_k) > 1:
            contig_list.append(cycle)
            break

print contig_list


