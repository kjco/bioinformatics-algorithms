END = '$'

class SuffixTree(object):

    def __init__(self):
        """Initalizes the tree with root (0) initialized."""
        self._nodes = [None]
        self.num_leaves = 0

    def _add_node(self, create_child_list=True):
        """Append a new node to the list."""
        value = None
        if create_child_list:
            value = dict()

        self._nodes.append(value)
        return value

    @property
    def size(self):
        return len(self._nodes)

    def print_tree(self):
        print 'SuffixTree has %d nodes (including root) and %d leaves.' % (self.size, self.num_leaves)
        print self._nodes

    def insert(self, seq, label):
        """Insert a seqence into the tree."""
        # The root node  is 0
        idx = 0
        for k in xrange(len(seq)):
            char = seq[k]
            # Get the children dictionary of the current node.
            child = self._nodes[idx]

            if not isinstance(child, dict):
                # The node has no child. Get a new dictionary
                self._nodes[idx] = dict()
                child = self._nodes[idx]

            if char in child:
                # Found the node with the same edge s.
                idx = child[char]
                continue

            shared_prefix = [x for x in child if x[0] == char]
            if not shared_prefix:
                # The node does not have children starting with s. Add a
                # node with the suffix.
                child[seq[k:]] = self.size
                idx = self.size
                self._add_node()
                break

            # Found node(s) starting with s.
            child[char] = self.size
            idx = self.size
            new_clist = self._add_node(create_child_list=True)
            for key in shared_prefix:
                new_clist[key[1:]] = child[key]
                del child[key]
            

        self._nodes[idx] = label
        self.num_leaves += 1


def main():
    seq = 'ATAAATG$'
    tree = SuffixTree()

    for i in xrange(len(seq)):
        tree.insert(seq[i:], i)

    tree.print_tree()


if __name__ == '__main__':
    main()
