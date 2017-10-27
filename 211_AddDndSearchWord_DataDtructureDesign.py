import collections


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_list = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.word_list[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        candidate = self.word_list[len(word)]
        word_dict = {}
        for i, v in enumerate(word):
            if v != '.':
                word_dict[i] = v
        for can in candidate:
            flag = True
            for key, val in word_dict.items():
                if can[key] != val:
                    flag = False
                    break
            if flag:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
