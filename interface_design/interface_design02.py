''' Question:
*   Implement a trie with insert, search, and startsWith methods.
*       interface Trie {
*           void insert(String word);
*           Boolean search(String word);
*           Boolean startsWith(String prefix);
*       }
'''


# Iterative solution
class Trie1:
    class TrieNode:
        def __init__(self):
            self.keys = {}
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.keys:
                node.keys[letter] = self.TrieNode()
            node = node.keys[letter]
        node.end = True

    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node.keys:
                return False
            node = node.keys[letter]
        return node.end

    def starts_with(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.keys:
                return False
            node = node.keys[letter]
        return True


# Recursive solution
class Trie2:
    class TrieNode:
        def __init__(self):
            self.keys = {}
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word, node=None):
        if node is None:
            node = self.root
        if not word:
            node.end = True
            return None
        if word[0] not in node.keys:
            node.keys[word[0]] = self.TrieNode()
        self.insert(word[1:], node.keys[word[0]])

    def search(self, word, node=None):
        if node is None:
            node = self.root
        if not word:
            return node.end
        if word[0] not in node.keys:
            return False
        return self.search(word[1:], node.keys[word[0]])

    def starts_with(self, prefix, node=None):
        if node is None:
            node = self.root
        if not prefix:
            return True
        if prefix[0] not in node.keys:
            return False
        return self.starts_with(prefix[1:], node.keys[prefix[0]])


# Test
if __name__ == '__main__':
    print('trie1_test')
    trie = Trie1()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('dog'))
    trie.insert('dog')
    print(trie.search('dog'))
    print(trie.search('app'))
    print(trie.starts_with('app'))
    print('-------------------------------')

    print('trie2_test')
    trie = Trie2()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('dog'))
    trie.insert('dog')
    print(trie.search('dog'))
    print(trie.search('app'))
    print(trie.starts_with('app'))
