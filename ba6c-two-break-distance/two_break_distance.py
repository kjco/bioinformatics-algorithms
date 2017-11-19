# read input into list of lists (genomes)
# all_genomes = [[genome1],[genome2],[genome3],...]
p = [1,2,3,4,5,6,1]
q1 = [1,-3,-6,-5,1]
q2 = [2,-4,2]


#print str(p[0]) + 'a'

d= dict()

def genome_edge(genome):
    for i in range(len(genome)-1):
        if genome[i] > 0 and genome[i+1] > 0:
            d[str(abs(genome[i]))+'b'] = str(abs(genome[i+1]))+'a'
        elif genome[i] < 0 and genome[i+1] > 0:
            d[str(abs(genome[i]))+'a'] = str(abs(genome[i+1]))+'a'
        elif genome[i] > 0 and genome[i+1] < 0:
            d[str(abs(genome[i]))+'b'] = str(abs(genome[i+1]))+'b'
        elif genome[i] < 0 and genome[i+1] < 0:
            d[str(abs(genome[i]))+'a'] = str(abs(genome[i+1]))+'b'
    
genome_edge(p)
genome_edge(q1)
genome_edge(q2)

print d

##test = {'apple':'orange', 'tea':'coffee', 'orange':'apple'}
##del test['apple']
##print test

two_edge_list = []
for k,v in d.iteritems():
    if d[k] in d and d[d[k]] == k:
        print k,v
        two_edge_list.append(k)

print two_edge_list

for n in two_edge_list:
    del d[n]

print d

d2 = dict()
for k,v in d.iteritems():
    d2[v] = k

print d2

#for k,v in d2.iteritems():
    

#d.update(d2)
#print d

node_list=[]
for k,v in d.iteritems():
    node_list.append(k)

count = 0

print '=========='

for a in node_list:
    k = a
    while True:
        remove_k = k
        print k
        print '--'
        k = d[k]
        print k
        print remove_k
        print d[remove_k]
        del d[remove_k]
        del d[d[remove_k]]
        print d
        node_list.remove(remove_k)
        if d[k] == a:
            count =+ 1
            break

print count



