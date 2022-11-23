class Node(object):
    def __init__(self, key, data = None):
        # key는 현재 알파벳, data는 삽입한 데이터가 있는지, children은 내 직속 자식들
        self.key = key
        self.data = data
        self.children = {}

class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        curr = self.head
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node(w)
            curr = curr.children[w]
        curr.data = word

    def search(self, word: str) -> bool:
        curr = self.head
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        if not curr.data:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)