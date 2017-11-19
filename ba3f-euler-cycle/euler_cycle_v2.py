
#d = {'0':['3'],'1':['0'],'2':['1','6'],'3':['2'],'4':['2'],'5':['4'],'6':['8'],'7':['9'],'8':['7'],'9':['6']}
#d = {0:[3],1:[0],2:[1,6],3:[2],4:[2],5:[4],6:[5,8],7:[9],8:[7],9:[6]}

d=dict()
with open('dataset_57_2.txt','r') as f:
   for line in f:
       chunks = line.strip().split('->')
       key = int(chunks[0])
       values = map(int, chunks[1].split(','))
       d[key] = values



def decide(input):
    for k,v in input.iteritems():
        if v:
            return True
    return False

cycle =[]
new_cycle = []
k = 0
# need to assign a random key in dictionary to k (k = random key) to initiate while loop

while decide(d):
    for i in range(len(cycle)):
        if d[cycle[i]]:
            k = cycle[i]
            new_cycle = cycle[i:len(cycle)]+cycle[0:i]
            #print new_cycle
            #print k
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
        #print d

    cycle = new_cycle + cycle
    #print cycle

#print cycle
print '->'.join(map(str, cycle))
