"""
まあwordsをtrieにしてもよいかも
TrieNodeのメソッドにaddとかがあったほうが良い
"""

class Node:
    def __init__(self):
        self.children = {}

# TLE
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        num_rows = len(board)
        num_cols = len(board[0])
        visited = [[False] * num_cols for _ in range(num_rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def add(r, c, node):
            visited[r][c] = True
            if board[r][c] not in node.children: 
                node.children[board[r][c]] = Node()
            
            for dx, dy in directions:
                next_r = r + dx
                next_c = c + dy
                if not (0 <= next_r < num_rows and 0 <= next_c < num_cols and not visited[next_r][next_c]):
                    continue
                add(next_r, next_c, node.children[board[r][c]])
            
            visited[r][c] = False
        
        def search(word):
            curr = root
            for c in word:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return True
        
        root = Node()
        for r in range(num_rows):
            for c in range(num_cols):
                add(r, c, root)
        
        detected_words = []
        for word in words:
            if search(word):
                detected_words.append(word)
        return detected_words

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
        
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()
        found_words = []
        
        def dfs(r, c, node, curr_word):
            if (
                r not in range(num_rows) or
                c not in range(num_cols) or
                (r, c) in visited or
                board[r][c] not in node.children or
                node.children[board[r][c]].refs == 0
            ): return
            
            visited.add((r, c))
            curr_word += board[r][c]
            node = node.children[board[r][c]]
            if node.is_word:
                found_words.append(curr_word)
                root.remove_word(curr_word)
            
            dfs(r + 1, c, node, curr_word)
            dfs(r - 1, c, node, curr_word)
            dfs(r, c + 1, node, curr_word)
            dfs(r, c - 1, node, curr_word)
            visited.remove((r, c))
        
        for r in range(num_rows):
            for c in range(num_cols):
                dfs(r, c, root, "")
        
        return found_words
