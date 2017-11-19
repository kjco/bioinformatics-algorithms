NUCLEOTIDE = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
REV_NUCLEOTIDE = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}

def _get_empty_child_list():
    """A helper function that returns an empty list for a new node"""
    return [None for x in range(len(NUCLEOTIDE))]

def get_new_trie():
    """Returns a new trie with root (0) initialized."""
    trie = [_get_empty_child_list()]
    return trie

def trie_insert_seq(trie, seq):
    # The root of trie is 0
    node = 0
    for s in seq:
        # Get the children list of the current node.
        children = trie[node]
        assert children
        c_index = NUCLEOTIDE[s]
        if not children[c_index]:
            # If no such child, make a node.
            new_node = len(trie)
            trie.append(_get_empty_child_list())
            children[c_index] = new_node

        # Move on to the child node.
        node = children[c_index]

def leaf_node(node_list):
    count = 0
    for n in node_list:
        if n:
            return False
    return True


def main():
    #text = 'AATCGGGTTCAATCGGGGT'
    #seqs = ['ATCG', 'GGGT']
    with open('dataset_93_6.txt','r') as f:
        text = f.readline().strip()
        seqs = []
        for line in f:
            pattern = line.strip()
            seqs.append(pattern)

    print seqs
    trie = get_new_trie()

    for seq in seqs:
        trie_insert_seq(trie, seq)

    #print trie
    #print leaf_node(trie[8])
    position = 0
    match_list = []

    while text:
        node = 0
        for i in xrange(len(text)):
            index = NUCLEOTIDE[text[i]]
            node = trie[node][index]

            if not node:
                break

            if leaf_node(trie[node]):
                match_list.append(position)
                break

        position += 1
        text = text[1:]

    print match_list
    print ' '.join(map(str, match_list))

##    for i in range(len(trie)):
##        for j in range(len(trie[i])):
##            if trie[i][j]:
##                a = i+1
##                b = trie[i][j] + 1
##                c = REV_NUCLEOTIDE[j]
##                print a, b, c

if __name__ == '__main__':
    main()



