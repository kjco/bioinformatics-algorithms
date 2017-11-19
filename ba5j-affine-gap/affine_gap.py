import sys

# 1: down, 1: right, 2: lower right
gap_ext = 1
gap_open = 11
min_int = -sys.maxint - 1


# Read the scoring matrix
d = dict()
with open('BLOSUM62.txt') as f:
    alphabets = f.readline().strip().split()

    for line in f:
        chars = line.strip().split()
        m = chars[0]
        scores = map(int, chars[1:])
        for i in range(len(scores)):
            d[(m, alphabets[i])] = scores[i]

#print d

with open('dataset_78_8.txt','r') as f:
    str1 = f.readline().strip()
    str2 = f.readline().strip()

##str1 = 'PRTEINS'
##str2 = 'PRTWPSEIN'

##str1 = 'ADDFFFSWDFVDFSWDHF'
##str2 = 'DFFFSFVQIFQDFSHE'

##str1 = 'QPYHSETSVDYPVGSEATTDNCNCLPTIWVTVFPMAIVMYLVPMFSMCWLKHAVGLDHLMMRWPWHNSFHDMMTNKNCWL'
##str2 = 'QPYHYPTKTTSVDYPVGSEAGTDNYNCLPTHTFQHFWVTVFEYVMYLMFSMDEVGQFKTWLKHIIAAGPVGLMMRWPMTNKSWWL'

##str1 = 'GCYTVVKFRFWGSCARPWKEYCHIMFERNHFPCQTIAPPLVCCEMANFTATLESHVQLVSFHNQIWPWGLKNSYMWALVHM'
##str2 = 'DVVKFRPWGSCARPWKEYCHSPVMFERNHYCQTIATAFTCKACEMANFTAYLESLRVVIVQYVSNKKSPFIWPWGLKNSYMWALVHM'

# Initialize the matrix
m_down = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
m_mid = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
m_right = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
b_down = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
b_mid = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
b_right = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]

# Initialize first rows/columns of backtrack matrix
for i in xrange(1,len(str1)+1):
    b_down[i][0] = 1
    b_mid[i][0] = 5

for i in xrange(1,len(str2)+1):
    b_right[0][i] = 3
    b_mid[0][i] = 6

# Initialize first rows/columns of scoring matrix
for i in xrange(1,len(str1)+1):
    m_down[i][0] = -(gap_open + (i-1)*gap_ext)
    m_mid[i][0] = -(gap_open + (i-1)*gap_ext)
    m_right[i][0] = min_int
#print m_down

for i in xrange(1,len(str2)+1):
    m_right[0][i] = -(gap_open + (i-1)*gap_ext)
    m_mid[0][i] = -(gap_open + (i-1)*gap_ext)
    m_down[0][i] = min_int
#print m_right

#print m_mid

#print 'matrix is %dx%d' % (len(m), len(m[0]))

for i in xrange(1, len(str1)+1):
    for j in xrange(1, len(str2)+1):
        m_down[i][j] = m_down[i-1][j] - gap_ext
        b_down[i][j] = 1

        if m_mid[i-1][j] - gap_open > m_down[i][j]:
            m_down[i][j] = m_mid[i-1][j] - gap_open
            b_down[i][j] = 2

        m_right[i][j] = m_right[i][j-1] - gap_ext
        b_right[i][j] = 3

        if m_mid[i][j-1] - gap_open > m_right[i][j]:
            m_right[i][j] = m_mid[i][j-1] - gap_open
            b_right[i][j] = 4

        m_mid[i][j] = m_down[i][j]
        b_mid[i][j] = 5

        if m_right[i][j] > m_mid[i][j]:
            m_mid[i][j] = m_right[i][j]
            b_mid[i][j] = 6

        if m_mid[i-1][j-1] + d[(str1[i-1], str2[j-1])] > m_mid[i][j]:
            m_mid[i][j] = m_mid[i-1][j-1] + d[(str1[i-1], str2[j-1])]
            b_mid[i][j] = 7


##print m_down
##print m_right
##print m_mid
#print b
#print m_mid[len(str1)][len(str2)]

# Determining max score and sink backtrack matrix sink_b
max_score = m_down[len(str1)][len(str2)]
sink_b = b_down
if m_right[len(str1)][len(str2)] > max_score:
    max_score = m_right[len(str1)][len(str2)]
    sink_b = b_right
if m_mid[len(str1)][len(str2)] >= max_score:
    max_score = m_mid[len(str1)][len(str2)]
    sink_b = b_mid

print max_score
#print sink_b

sys.setrecursionlimit(5000)

# Backtracking
def OutputLCS(path1, path2, b, i, j):
#    print i, j, b[i][j]
#     if i == 0 or j == 0:
#         return
    if i == 0 and j == 0:
        return
    elif b[i][j] == 1:
        OutputLCS(path1, path2, b_down, i-1, j)
        path1.append(str1[i-1])
        path2.append('-')
    elif b[i][j] == 2:
        OutputLCS(path1, path2, b_mid, i-1, j)
        path1.append(str1[i-1])
        path2.append('-')
    elif b[i][j] == 3:
        OutputLCS(path1, path2, b_right, i, j-1)
        path1.append('-')
        path2.append(str2[j-1])
    elif b[i][j] == 4:
        OutputLCS(path1, path2, b_mid, i, j-1)
        path1.append('-')
        path2.append(str2[j-1])
    elif b[i][j] == 5:
        OutputLCS(path1, path2, b_down, i, j)
        path1.append('')
        path2.append('')
    elif b[i][j] == 6:
        OutputLCS(path1, path2, b_right, i, j)
        path1.append('')
        path2.append('')
    elif b[i][j] == 7:
        OutputLCS(path1, path2, b_mid, i-1, j-1)
        path1.append(str1[i-1])
        path2.append(str2[j-1])


##    elif b[i][j] == 1:
##        OutputLCS(path1, path2, b, i, j-1)
##        path1.append('-')
##        path2.append(str2[j-1])
##    else:
##        OutputLCS(path1, path2, b, i-1, j-1)
##        path1.append(str1[i-1])
##        path2.append(str2[j-1])

path1 = []
path2 = []

OutputLCS(path1,  path2, sink_b, len(str1), len(str2))
print ''.join(path1)
print ''.join(path2)
#print len(path)
