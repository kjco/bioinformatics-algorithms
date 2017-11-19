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

def main():
    #seqs = ['GGTA', 'CG', 'GGC']
    seqs = [line.strip() for line in open('dataset_93_3.txt','r')]
    trie = get_new_trie()

    for seq in seqs:
        trie_insert_seq(trie, seq)

    #print trie

    for i in range(len(trie)):
        for j in range(len(trie[i])):
            if trie[i][j]:
                a = i+1
                b = trie[i][j] + 1
                c = REV_NUCLEOTIDE[j]
                print a, b, c

if __name__ == '__main__':
    main()



