import sys
import math
sys.setrecursionlimit(2000)


# 0: down, 1: right, 2: lower right
SIGMA = 5
# Number of columns to keep in the score matrix
BUF_WIDTH = 2

def compute_scores(str1, str2, m, b):
    """Populates the score and backtrack matrices.

    Args:
        str1: first string.
        str2: second string.
        m: score matrix.
        b: backtrack matrix.
    """
    last_col = 0
    for j in xrange(1, len(str2)+1):
        k = j % BUF_WIDTH
        k_prev = (j - 1) % BUF_WIDTH
        # Initialize the boundaries.
        m[0][k] = -SIGMA*j

        for i in xrange(1, len(str1)+1):
            # Case 0
            m[i][k] = m[i-1][k] - SIGMA
            b[i] = 0

            # Case 1
            score = m[i][k_prev] - SIGMA
            if score > m[i][k]:
                m[i][k] = score
                b[i] = 1

            # Case 2
            score =  m[i-1][k_prev] + d[(str1[i-1], str2[j-1])]
            if score > m[i][k]:
                m[i][k] = score
                b[i] = 2

            last_col = k

#         print [m[x][k] for x in range(len(str1)+1)]
    return last_col


def middle_edge(top, bottom, left, right):
    """Returns the middle edge of the area."""

    length = bottom - top +1
    width = right - left + 1
    mid = left + width/2  -1
    l_width = mid - left + 1
    r_width = right - mid

    # Initialize the matrices.
    m = [[0 for j in range(BUF_WIDTH)] for i in range(length+1)]
    # We need only one column for backtracking.
    b = [0 for i in range(length+1)]
    r = [[0 for j in range(BUF_WIDTH)] for i in range(length+1)]
    # We need only one column for backtracking.
    br = [0 for i in range(length+1)]

    for i in xrange(1, length+1):
        m[i][0] = -SIGMA*i
    for i in xrange(1, length+1):
        r[i][0] = -SIGMA*i
 
    # Compute scores from source to mid column.
    stra, strb = str1[top:bottom+1], str2[left:mid+1]
    k = compute_scores(stra, strb, m, b)
    l_mid_list = []
    for i in range(length+1):
        l_mid_list.append(m[i][k])

    # Compute scores from sink to mid column.
    rev1 = (str1[top:bottom+1])[::-1]
    rev2 = (str2[mid+1:right+1])[::-1]
    k = compute_scores(rev1, rev2, r, br)
    r_mid_list = []
    for i in range(length+1):
        r_mid_list.append(r[i][k])

    rev_r_mid_list = r_mid_list[::-1]

    sum_list = []
    for i in range(length):
        sum_list.append(l_mid_list[i]+rev_r_mid_list[i])

#     for x in  r:
#         print x
#     #print max(sum_list)
#     print l_mid_list
#     print r_mid_list
#     print sum_list
    max_index = sum_list.index(max(sum_list))
    y = width/2 + left
    mid_edge_src = (max_index, y)


    x = length - max_index
    if br[x] == 2:
        row = max_index + 1
        col = y + 1
    elif br[x] == 1:
        row = max_index
        col = y + 1
    elif br[x] == 0:
        row = max_index + 1
        col = y
    else:
        raise ValueError('Unexpected value: br[%d] = %d' % (x, br[x]))

    mid_edge_dest = (row, col)
#     print '(%s, %s)' % (str(row), str(col))

    return (mid_edge_src, mid_edge_dest)


#================ MAIN =======================

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

# Read input strings
#with open('dataset_79_12.txt','r') as f:
##with open('linear_space.txt','r') as f:
##    str1 = f.readline().strip()
##    str2 = f.readline().strip()

str1 = 'PLEASANTLY'
str2 = 'MEANLY'

#===============================================

##mid_edge_src, mid_edge_dest = middle_edge(0, len(str1)-1, 0, len(str2)-1)
##print mid_edge_src
##print mid_edge_dest
##
##print mid_edge_src[0]

def seq_align(src,dest):
    diff0 = dest[0] - src[0]
    diff1 = dest[1] = src[1]
    if diff0 == 1 and diff1 == 0:
        path1.append('-')
        path2.append(str2[src[0]])
    elif diff0 == 0 and diff1 == 1:
        path1.append(str1[src[1]])
        path2.append('-')
    elif diff0 == 1 and diff1 == 1:
        path1.append(str1[src[1]])
        path2.append(str2[src[0]])


def LSA(top, bottom, left, right):
    if left == right:
        seq_align(mid_edge_src,mid_edge_dest)
        return
    mid_edge_src,mid_edge_dest = middle_edge(top, bottom, left, right)
    midNode = mid_edge_src[0]
    middle = mid_edge_src[1]

    LSA(top, midNode, left, middle)

    LSA(mid_edge_dest[0],bottom,mid_edge_dest[1],right)


path1 = []
path2 = []

LSA(0, len(str1), 0, len(str2))

print ''.join(path1)
print ''.join(path2)
