# Programming solution for:
#   Reconstruct a String from its k-mer Composition
#   http://rosalind.info/problems/ba3h/
#
# **String Reconstruction Problem**
# 
# Reconstruct a string from its k-mer composition.
#   - Given: An integer k followed by a list of k-mers Patterns.
#   - Return: A string Text with k-mer composition equal to Patterns. (If multiple
#     answers exist, you may return any one.)


def out_node(input,new_input):
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
with open('dataset_57_6.txt','r') as f:
   for line in f:
       chunks = line.strip().split('->')
       key = chunks[0].strip()
       value = [x.strip() for x in chunks[1].split(',')]
       d[key] = value

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

if last_node in d:
    d[last_node].append(first_node)
else:
    d[last_node] = [first_node]


def decide(input):
    for k,v in input.iteritems():
        if v:
            return True
    return False

cycle =[]
new_cycle = []
k = last_node
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


#break_point = None
for i in range(len(cycle)-1):
    if cycle[i] == last_node and cycle[i+1] == first_node:
        break_point = i

output_cycle = cycle[break_point+1:]+cycle[:break_point+1]
#print output_cycle
string = output_cycle[0]
for i in range(len(output_cycle)-1):
    n = output_cycle[i+1][-1]
    string = string + n

print string
#print '->'.join(output_cycle)
