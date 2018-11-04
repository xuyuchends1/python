from collections import Counter

list_a = [[ 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3 ],
          [4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3],
          [ 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]]

d=Counter()
for l in [ Counter(l) for l in list_a]:
     d+=l
value=sorted(d.items(), key=lambda d :d[0])

value[0][1]
pass
