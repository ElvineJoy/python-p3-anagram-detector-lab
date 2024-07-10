# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, word):
        anagram = []
        for letter in word:
            if sorted(letter) == self.sorted_word:
                anagram.append(letter)
        return anagram
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana', 'silent']))