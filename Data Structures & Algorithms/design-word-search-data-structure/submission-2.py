class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                new = TrieNode()
                curr.children[index] = new
            curr = curr.children[index]
        curr.isEndOfWord = True
        return
        

    def search(self, word: str, start: TrieNode = None) -> bool:
        curr = self.root if start is None else start
        for i in range(len(word)):
            char = word[i]
            if char == ".":
                starts = [c for c in curr.children if c is not None]
                if not starts: return False
                if i == len(word)-1:
                    return any(c.isEndOfWord for c in starts)
                else:
                    return any(self.search(word[i+1:],s) for s in starts)
            else:
                index = ord(char) - ord('a')
                if curr.children[index] is None:
                    return False
                curr = curr.children[index]
        return curr.isEndOfWord
        
