sentence = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter Piper picked a peck of pickled peppers Wheres the peck of pickled peppers Peter Piper picked"

word_dict={}
for word in sentence.split():
    if word not in word_dict:
        word_dict[word]=1
    else:
        word_dict[word]+=1


print(word_dict)


from collections import defaultdict
word_dict_2=defaultdict(int)

for word in sentence.split():
    word_dict_2[word]+=1

print(word_dict_2)
pass
