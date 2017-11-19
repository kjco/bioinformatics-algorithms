# Programming solution for:
#   Find an Eulerian Path in a Graph 
#   http://rosalind.info/problems/ba3g
#
# In "Find an Eulerian Cycle in a Graph", we defined an Eulerian cycle. A path
# that traverses each edge of a graph exactly once (but does not necessarily
# return to its starting node is called an Eulerian path.
#
# **Eulerian Path Problem**
#
# Find an Eulerian path in a graph.
#   - Given: A directed graph that contains an Eulerian path, where the graph is
#     given in the form of an adjacency list.
#   - Return: An Eulerian path in this graph.

def out_node(input, new_input):
    for k,v in input.iteritems():
        if k not in new_input:
            return k
        elif len(input[k]) > new_input[k]:
            return k

def in_node(input, new_input):
    for k,v in new_input.iteritems():
        if k not in input:
            return k
        elif len(input[k]) < new_input[k]:
            return k

#d = {0:[2],1:[3],2:[1],3:[0,4],6:[3,7],7:[8],8:[9],9:[6]}

d=dict()
with open('dataset_57_5.txt','r') as f:
   for line in f:
       chunks = line.strip().split('->')
       key = int(chunks[0])
       values = map(int, chunks[1].split(','))
       d[key] = values

in_d = dict()

for k,v in d.iteritems():
    for node in v:
        if node not in in_d:
            in_d[node] = 1
        elif node in in_d:
            in_d[node] += 1

last_node = in_node(d, in_d)
first_node = out_node(d, in_d)
#print in_node(d, in_d)
#print out_node(d, in_d)

#d[last_node] = [first_node]
# the above is wrong, please beware!
d[last_node].append(first_node)

def decide(input):
    for k,v in input.iteritems():
        if v:
            return True
    return False

cycle =[]
new_cycle = []
k = first_node
# need to assign a random key in dictionary to k (k = random key) to initiate while loop

while decide(d):
    for i in range(len(cycle)):
        if d[cycle[i]]:
            k = cycle[i]
            new_cycle = cycle[i:len(cycle)]+cycle[0:i]
            break
    ki = k
    cycle = [ki]
    while True:
        orig_k = k
        k = d[k][0]
        d[orig_k].remove(d[orig_k][0])
        if k == ki:
            break
        cycle.append(k)

    cycle = new_cycle + cycle


for i in range(len(cycle)-1):
    if cycle[i] == last_node and cycle[i+1] == first_node:
        break_point = i
    
output_cycle = cycle[break_point+1:]+cycle[0:break_point+1]
#print output_cycle
print '->'.join(map(str, output_cycle))
