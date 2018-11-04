import re
import reprlib
RE_WORD=re.compile('\w+')

class Sentence:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)

    # def __getitem__(self, item):
    #     return self.words[item]

    def __len__(self):
        return len(self.words)

    # def __iter__(self):
    #     # for word in self.words:
    #     #     yield  word
    #     # return
    #     return iter(self.words)



s=Sentence('the time has come,the walrus said')
for word in iter(s.words):
    print (word)

pass