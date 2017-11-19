
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

p = []
with open('dataset_87_2.txt') as f:
    num_list = f.readline().strip('()\n ').split(' ')
    p = map(int, num_list)

def flip_sign(n):
    return n*(-1)

for i in range(len(p)):
    if p[i] == i+1:
        continue
    elif p[i] == -(i+1):
        p[i] = -p[i]
        seq.append(list(p))
        continue

    for j in range(i, len(p)):
        if abs(p[j]) == i + 1:
            #print i,j
            p1 = p[:i]
            p2 = p[i:j+1]
            p2 = p2[::-1]
            p2 = map(flip_sign, p2)
            p3 = p[j+1:]
            #print p1, p2, p3
            p = p1 + p2 + p3
            #print p
            seq.append(list(p))
            if p[i] < 0:
                p[i] = -p[i]
                seq.append(list(p))
#print p
#print seq


str_seq = [map(int_to_str, x) for x in seq]

for x in str_seq:
    print '(%s)' % ' '.join(x)
