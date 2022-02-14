import copy


def Merge(dict1, dict2):
    return (dict2.update(dict1))


def split(word):
    return [char for char in word]


class Solution(object):
    hashSet = {}
    max = []

    def ladderLength(self, beginWord, endWord, wordList):
        self.max = []
        if len(beginWord) != len(endWord):
            return 0
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)

        endWord = split(endWord)
        hashSet = {}
        u_alpha = []
        for w in wordList:
            u_alpha += split(w)

        u_alpha = list(set(u_alpha))

        for word in wordList:
            ori = split(word)
            for index in range(len(endWord)):
                word = copy.deepcopy(ori)
                for z in range(len(u_alpha)):
                    word[index] = u_alpha[z]
                    if ''.join(word) in wordList:
                        arr = hashSet.get(''.join(ori), [])
                        if ''.join(word) != ''.join(ori):
                            arr.append(''.join(word))
                            hashSet[''.join(ori)] = list(set(arr))

        if ''.join(beginWord) not in hashSet.keys():
            return 0

        self.hashSet = hashSet
        for x in hashSet.keys():
            print(f"{x} => {hashSet.get(x)}")

        self.df(''.join(beginWord), ''.join(endWord), 1)
        print(max(self.max))

    def df(self, start, endWord, level, visited=[]):
        visited.append(start)
        for x in self.hashSet.get(start):
            print(x)
            if x == endWord:
                self.max.append(level)
            if x not in visited:
                 self.df(x, endWord, level+1, visited)
        self.max.append(0)



s = Solution()
# print(s.ladderLength("a", "c", ["a", "b", "c"]))
print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(s.ladderLength("hot", "dog", ["hot", "dog"]))
# print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
# print(s.ladderLength("hot", "dog", ["hot", "dog", "dot"]))
