#!/bin/python3

import os

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#


class NodeTrie:
    def __init__(self):
        self.children = [None] * 26
        self.is_leaf = False
        self.count_prefix = 0

class Trie:
    def __init__(self):
        self.root = NodeTrie()

    def insert(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = NodeTrie()
            curr = curr.children[index]
            curr.count_prefix += 1
        curr.is_leaf = True
        return None

    def search(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.is_leaf

    def count_prefix(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return curr.count_prefix


def contacts(queries):
    results = []
    t = Trie()
    for (action, key) in queries:
        if action == 'add':
            t.insert(key)
        elif action == 'find':
            results.append(t.count_prefix(key))
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    queries_rows = int(input().strip())
    queries = []
    for _ in range(queries_rows):
        queries.append(input().rstrip().split())
    result = contacts(queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
