##str1 = 'PLEASANTLY'
##str2 = 'MEANLY'


with open('dataset_77_3.txt','r') as f:
    str1 = f.readline().strip()
    str2 = f.readline().strip()

# Initialize the matrix
m = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
#b = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
# m = [ [0] * (len(str2)+1) ] * (len(str1)+1)
# b = [ [0] * (len(str2)+1) ] * (len(str1)+1)

#print 'matrix is %dx%d' % (len(m), len(m[0]))

for j in range(len(str2)+1):
    m[0][j] = j

for i in range(len(str1)+1):
    m[i][0] = i

#print m

for i in xrange(1, len(str1)+1):
    for j in xrange(1, len(str2)+1):
        m[i][j] = m[i-1][j] + 1

        if m[i][j-1] + 1 < m[i][j]:
            m[i][j] = m[i][j-1] + 1

        if m[i-1][j-1] + 1 < m[i][j]:
            m[i][j] = m[i-1][j-1] + 1

        if str1[i-1] == str2[j-1] and m[i-1][j-1]+0 < m[i][j]:
            m[i][j] = m[i-1][j-1] + 0

        #print i,j, m[i][j], b[i][j]

#print b
#print m
print m[len(str1)][len(str2)]
