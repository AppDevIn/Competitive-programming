from typing import List

class Word:
    def __init__(self, word="", value=0):
        self.word = word
        self.value = value
    
class TrieNode:
    def __init__(self):
        self.lastWord = False
        self.child = {}
        self.word = None
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insertionSort(self, value, arr):
        index = 0
        while index < len(arr) and (value.value < arr[index].value or (value.value == arr[index].value and value.word >= arr[index].word)):
            index += 1
        arr.insert(index, value)

    def insert(self, word: str, value) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.lastWord = True
        if curr.word:
            curr.word.value += 1
        else: 
            curr.word = Word(word, value)
    
    def searchPrefix(self, prefix: str) -> TrieNode:
        curr = self.root
        for c in prefix:
            if c in curr.child:
                curr = curr.child[c]
            else:
                return None
        return curr
    
    def collectWords(self, node: TrieNode, result: List[Word]) -> None:
        if node.word:
            self.insertionSort(node.word, result)
        for child in node.child.values():
            self.collectWords(child, result)
    
    def values(self, root: TrieNode) -> List[str]:
        if not root:
            return []
        result = []
        self.collectWords(root, result)
        
        return [result[i].word for i in range(min(3, len(result)))]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.currNode = self.trie.root
        self.currentInput = ""
        
        for index in range(len(sentences)):
            self.trie.insert(sentences[index], times[index])
        

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.currentInput, 1)
            self.currNode = self.trie.root
            self.currentInput = ""
            
            return []
        
        self.currentInput += c
        self.currNode = self.trie.searchPrefix(self.currentInput)
        if self.currNode:
            return self.trie.values(self.currNode)
        else:
            return []

