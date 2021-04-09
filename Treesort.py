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

liste = DictBinTree.orderedTraversal(dictionary)
while i < n:
    print(liste[0])
    n = n+1
