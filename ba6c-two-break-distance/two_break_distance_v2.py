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
p = [1,2,3,4,5,6,1]
q1 = [1,-3,-6,-5,1]
q2 = [2,-4,2]


#print str(p[0]) + 'a'

d= dict()


    
genome_edge(p)
genome_edge(q1)
genome_edge(q2)

print d

##test = {'apple':'orange', 'tea':'coffee', 'orange':'apple'}
##del test['apple']
##print test

two_edge_list = []
for k, v_list in d.iteritems():
    for v in v_list:
        if v in d and k in d[v]:
            print '@@@ %s %s' % (k,v)
            two_edge_list.append((k,v))

print two_edge_list
# Number of two-edge cycles is len(two_edge_list)/2

for k, v in two_edge_list:
    delete_dict(d, k, v)

print d

for k, v_list in d.items():
    for v in v_list:
        append_dict(d, v, k)

print d


node_list=[]
for k, v in d.iteritems():
    node_list.append(k)

count = 0

print '=========='

while node_list:
    k = node_list[0]
    a = node_list[0]
    while True:
        remove_k = k
        remove_v = d[remove_k][0]
        print k
        print '--'
        k = d[k][0]
        print k
        print remove_k
        print d[remove_k][0]
        delete_dict(d, remove_k, remove_v)
        delete_dict(d, remove_v, remove_k)
        print d
        node_list.remove(remove_k)
        if d[k][0] == a:
            delete_dict(d, k, a)
            delete_dict(d, a, k)
            count += 1
            print '***'
            print count
            break

print count



