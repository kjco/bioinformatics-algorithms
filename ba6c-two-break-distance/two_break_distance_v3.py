def append_dict(d, key, value):
    if key in d:
        if not value in d[key]:
            d[key].append(value)
    else:
        d[key] = [value]

def delete_dict(d, key, value):
    if key in d:
        # Note: remove() only removes the fisrt occurence of the
        # element in the list. However, we should not have duplicated
        # values in the list.
        d[key].remove(value)

        # Delete the entry if no value is in it.
        if d[key] == []:
            del d[key]


def genome_edge(genome):
    for i in range(len(genome)-1):
        k = str(abs(genome[i]))
        v = str(abs(genome[i+1]))
        if genome[i] > 0 and genome[i+1] > 0:
            append_dict(d, k + 'b', v + 'a')
        elif genome[i] < 0 and genome[i+1] > 0:
            append_dict(d, k + 'a', v + 'a')
        elif genome[i] > 0 and genome[i+1] < 0:
            append_dict(d, k + 'b', v + 'b')
        elif genome[i] < 0 and genome[i+1] < 0:
            append_dict(d, k + 'a', v + 'b')

#====================================================

# read input into list of lists (genomes)
# all_genomes = [[genome1],[genome2],[genome3],...]
##p = [1,2,3,4,5,6,1]
##q1 = [1,-3,-6,-5,1]
##q2 = [2,-4,2]

genome_list = []
with open('dataset_89_1.txt') as f:
    for line in f:
        t_list = line.strip('()\n').split('(')
        for t in t_list:
            t = map(int, t.strip('()').split())
            t.append(t[0])
            genome_list.append(t)


d= dict()

for i in genome_list:
    genome_edge(i)

#print d
    
##genome_edge(p)
##genome_edge(q1)
##genome_edge(q2)

#print d

##test = {'apple':'orange', 'tea':'coffee', 'orange':'apple'}
##del test['apple']
##print test

two_edge_list = []
for k, v_list in d.iteritems():
    for v in v_list:
        if v in d and k in d[v]:
            #print '@@@ %s %s' % (k,v)
            two_edge_list.append((k,v))

#print two_edge_list
# Number of two-edge cycles is len(two_edge_list)/2

for k, v in two_edge_list:
    delete_dict(d, k, v)

#print d

for k, v_list in d.items():
    for v in v_list:
        append_dict(d, v, k)

#print d

blocks = len(d.keys())/2 + len(two_edge_list)/2


##node_list=[]
##for k, v in d.iteritems():
##    node_list.append(k)

count = 0

#print '=========='

while d.keys():
    initiate_node = d.keys()[0]
    k = initiate_node
    while True:
        assert len(d[k]) <= 2
        k_next = d[k][0]
        v = d[k][0]
        #print '(%s, %s), k_next: %s' % (k, v, k_next)
        delete_dict(d, k, v)
        delete_dict(d, v, k)
        if k_next == initiate_node:
            count += 1
            #print '**count is %d' % count
            break
        k = k_next

print count
print len(two_edge_list)/2
cycle = count + len(two_edge_list)/2
print cycle
print blocks - cycle
