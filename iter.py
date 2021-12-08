

class Sentence():

    def __init__(self, sent):
        self.sent = sent
        self.list = self.sent.split()

    def __iter__(self):
        return iter(self.list)


# print("This is a test".split())

my_sentence = Sentence("This is a test")
for word in my_sentence:
    print(word)
