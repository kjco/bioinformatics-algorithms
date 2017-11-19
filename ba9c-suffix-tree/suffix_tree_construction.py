import suffix_tree

#text = 'ATAAATG$'

#with open('suffixTree.txt', 'r') as f:
with open('dataset_96_5.txt', 'r') as f:
    text = f.readline().strip()

tree = suffix_tree.SuffixTree()

for i in xrange(len(text)):
    tree.insert(text[i:],i)

#tree.print_tree()

#print tree._nodes[0].keys()

for item in tree._nodes:
    if isinstance(item, dict):
        print '\n'.join(item.keys())


