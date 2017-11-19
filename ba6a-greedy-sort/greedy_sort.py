
#with open('dataset_57_2.txt','r') as f:
#    p = f.strip('()\n').split(' ')

#p = [line.strip('()\n').split(' ') for line in open('dataset_52_7.txt','r')]
#p = [-3, +4, +1, +5, -2]
p = [-1, -2, -6, -5, -4, +3, -10, -9, -8, -7]

seq = []
##print len(p)
##print abs(p[0])
##print p[:0:] + p[2::-1] + p[3::]
##print p[:1]
##print p[0:3]
##print p[3::]

##for i in range(len(p)):
##    p[i] = -p[i]
##
##print p
##print p[1:5]
##print p[5:]

for i in range(len(p)):
    if i+1 == p[i]:
        continue
    for j in range(len(p)):
        if i+1 == abs(p[j]):
            #print i,j
            p1 = p[:i]
            p2 = p[i:j+1]
            p2 = p2[::-1]
            for n in range(len(p2)):
                p2[n] = -p2[n]
            p3 = p[j+1:]
            #print p1, p2, p3
            p = p1 + p2 + p3
            print p
            seq.append(list(p))
            if p[i] < 0:
                p[i] = -p[i]
                print p
                seq.append(list(p))

#print p
print seq
