

#d = {'0':['2'],'1':['3'],'2':['1'],'3':['0','4'],'6':['3','7'],'7':['8'],'8':['9'],'9':['6']}
d = {0:[2],1:[3],2:[1],3:[0,4],6:[3,7],7:[8],8:[9],9:[6]}

in_d = dict()


##for k,v in d.iteritems():
##    for node in v:
##        print node
##        in_d[node] += 1
##
##print in_d

#d = {'a':1,'b':0}

#d['a'] += 1

#print d['a']

for k,v in d.iteritems():
    for node in v:
        if node not in in_d:
            in_d[node] = 1
        elif node in in_d:
            in_d[node] += 1

print in_d

for k,v in d.iteritems():
    if len(d[k]) != in_d[k]:
        print k

for k,v in in_d.iteritems():
    if k not in d:
        print k
    
    
