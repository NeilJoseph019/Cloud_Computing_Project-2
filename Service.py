from itertools import permutations
from itertools import combinations

class Service(object):

    def sorted_key(self, word):
        chars = [c for c in word]
        chars.sort()
        return "".join(chars)

    def possiblepermutations(self,text):

        return [''.join(p) for p in permutations(text)]


    def subWordSort(self,word):
        listWord = list(word)
        word_keys = []
        for i in range(3,len(word)+1):
            temp=(["".join(c)for c in permutations(word,i)])
            for c in temp:
                word_keys.append(c)
        return word_keys