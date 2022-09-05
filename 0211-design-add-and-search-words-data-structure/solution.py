# this works, but takes too long on the entire test set, so not sure it
# actually works on all cases.  i think a prefix/suffix tree like this is the
# way to go, though, this just isn't the best implementation
class WordDictionary1:
    def __init__(self):
        self._children = {}

    def addWord2(self, word: str) -> None:
        if word[0] not in self._children:
            self._children[word[0]] = WordDictionary1()

        if len(word) > 1:
            self._children[word[0]].addWord2(word[1:])

    def addWord(self, word: str) -> None:
        self.addWord2(word + "X")

    def search2(self, word: str) -> bool:
        if len(word) == 1:
            return word in self._children
        else:
            if word[0] == ".":
                for v in self._children.values():
                    if v.search2(word[1:]):
                        return True
                return False
            else:
                if word[0] in self._children:
                    return self._children[word[0]].search2(word[1:])
                else:
                    return False

    def search(self, word: str) -> bool:
        return self.search2(word + "X")

# this works, but is probably not optimal.  it's great on memory, but is slow
# on the entire test set
class WordDictionary2:
    def __init__(self):
        self._words = []
        self._n_words = [0] * 25
        self._index = [{c: set() for c in "abcdefghijklmnopqrstuvwxyz"} for i in range(25)]

    def addWord(self, word: str) -> None:
        self._words.append(word)
        self._n_words[len(word) - 1] += 1
        for i, c in enumerate(word):
            self._index[i][c].add(len(self._words) - 1)

    def search(self, word: str) -> bool:
        if self._n_words[len(word) - 1] == 0:
            return False

        all_wildcard = True
        s = None

        for i, c in enumerate(word):
            if c != ".":
                all_wildcard = False

            if s is None:
                if c != ".":
                    s = self._index[i][c]

            else:
                if c != ".":
                    s = s & self._index[i][c]

                if len(s) == 0:
                    return False

        if all_wildcard:
            return True

        if s is None:
            return False

        for i in s:
            if len(word) == len(self._words[i]):
                for a, b in zip(word, self._words[i]):
                    if a != "." and a != b:
                        return False
                return True

        return False

def main() -> None:
    wordDictionary = WordDictionary2()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))
    print(wordDictionary.search("bad"))
    print(wordDictionary.search(".ad"))
    print(wordDictionary.search("b.."))

if __name__ == '__main__':
    main()
