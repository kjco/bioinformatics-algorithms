#p = [+3,+4,+5,-12,-8,-7,-6,+1,+2,+10,+9,-11,+13,+14]

p = []
with open('dataset_88_1.txt') as f:
    num_list = f.readline().strip('()\n ').split(' ')
    p = map(int, num_list)


count = 0

for i in range(len(p)-1):
    if p[i+1] == p[i] + 1 or p[i+1] == p[i] - 1:
        continue
    else:
        count += 1

print count
