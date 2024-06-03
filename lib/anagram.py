# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):

        return [word for word in words if sorted(word.lower()) == sorted(
            self.word.lower()) and word.lower() != self.word.lower()]



# listen = Anagram("google")
# print(listen.match(["enlist", "google", "glean"]))


# test = [word for word in 'angel']
# print(listen.word)

# anagram = Anagram("listen")
# toMatch = ["enlists", "google", "inlets", "banana", "silent","listen"]
# result = anagram.match(toMatch)
# print(result)
