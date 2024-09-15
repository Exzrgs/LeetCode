class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(curr, word):
            for i, c in enumerate(word):
                if c == ".":
                    for node in curr.children:
                        if node and dfs(node, word[i + 1:]):
                            return True
                    return False
                else:
                    index = ord(c) - ord("a")
                    if curr.children[index] is None:
                        return False
                    curr = curr.children[index]
            return curr.end
        
        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
