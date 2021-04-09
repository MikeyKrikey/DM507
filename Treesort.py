'''
Gruppe:

Stine Holz Meinhardt Gregersen, sgreg18
Michael Kristensen, mickr19
Hanna Bruun-Schmidt, habru19

'''

import sys
import DictBinTree

dictionary = DictBinTree.createEmptyDict()

n = 0
for line in sys.stdin:
    DictBinTree.insert(dictionary,int(float(line)))
    n = n+1

print()
liste = DictBinTree.orderedTraversal(dictionary)
i = 0
while i < n:
    print(liste[i])
    i = i+1
