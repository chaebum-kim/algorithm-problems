''' Question:
*   Implement a trie with insert, search, and startsWith methods.
*       interface Trie {
*           void insert(String word);
*           Boolean search(String word);
*           Boolean startsWith(String prefix);
*       }
'''


class Trie:
    class TrieNode:
        def __init__(self):
            self.keys = {}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word, node=None):
        if node is None:
            node = self.root
        if not word:
            node.is_end = True
            return None
        elif node.keys.get(word[0]) is None:
            node.keys[word[0]] = self.TrieNode()
            self.insert(word[1:], node.keys[word[0]])
        else:
            self.insert(word[1:], node.keys[word[0]])

    def search(self, word, node=None):
        if node is None:
            node = self.root
        if not word:
            return True if node.is_end else False
        elif node.keys.get(word[0]) is None:
            return False
        else:
            return self.search(word[1:], node.keys[word[0]])

    def starts_with(self, prefix, node=None):
        if node is None:
            node = self.root
        if not prefix:
            return True
        elif node.keys.get(prefix[0]) is None:
            return False
        else:
            return self.starts_with(prefix[1:], node.keys[prefix[0]])


# Test
if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('dog'))
    trie.insert('dog')
    print(trie.search('dog'))
    print(trie.search('app'))
    print(trie.starts_with('app'))
