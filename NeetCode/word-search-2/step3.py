class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.refs = 0
    
    def add_word(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.is_word = True
    
    def remove_word(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            curr = curr.children[c]
            curr.refs -= 1
        curr.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)
        
        found_words = []
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()
        
        def dfs(r, c, node, word):
            if (
                r not in range(num_rows) or
                c not in range(num_cols) or
                (r, c) in visited or
                board[r][c] not in node.children or
                node.children[board[r][c]].refs == 0
            ): return
            
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.is_word:
                found_words.append(word)
                root.remove_word(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
        
        for r in range(num_rows):
            for c in range(num_cols):
                dfs(r, c, root, "")
        
        return found_words
