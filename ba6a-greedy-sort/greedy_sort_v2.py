
#p = [-3, +4, +1, +5, -2]

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

def int_to_str(d):
    if d > 0:
        return '+%s' % str(d)
    else:
        return str(d)

def str_to_int(s):
    if s[0] == '-':
        return int(s[1:])
    else:
        return int(s)

p = []
with open('dataset_87_2.txt') as f:
    for line in f:
        t = line.strip('()\n ').split(' ')
        for x in t:
            p.append(str_to_int(x))
#         p.append([map(str_to_int, x) for x in t])
#         print p

#print p

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
            #print p
            seq.append(list(p))
            if p[i] < 0:
                p[i] = -p[i]
                #print p
                seq.append(list(p))

#print p
#print seq


str_seq = [map(int_to_str, x) for x in seq]

for x in str_seq:
    print '(%s)' % ' '.join(x)
