
#d = {'0':['3'],'1':['0'],'2':['1','6'],'3':['2'],'4':['2'],'5':['4'],'6':['8'],'7':['9'],'8':['7'],'9':['6']}
d = {0:[3],1:[0],2:[1,6],3:[2],4:[2],5:[4],6:[8],7:[9],8:[7],9:[6]}

def decide(input):
    for k,v in input.iteritems():
        if v:
            return True
    return False

k = 0
ki = 0
cycle = [ki]

while True:
    ori_k=k
    k = d[k][0]
    if k == ki:
        break
    cycle.append(k)
    d[ori_k].remove(d[ori_k][0])


print cycle
print d

for i in range(len(cycle)):
    if d[cycle[i]]:
        k = cycle[i]
        new_cycle = cycle[i:len(cycle)]+cycle[0:i]
        break

print i
print new_cycle

