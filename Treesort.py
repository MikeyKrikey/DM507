'''
Gruppe:

Stine Holz Meinhardt Gregersen, sgreg18
Michael Kristensen, mickr19
Hanna Bruun-Schmidt, habru19

'''

import sys
import DictBinTree

dictionary = DictBinTree.createEmptyDict() #lav tom dictionary

n = 0
for line in sys.stdin:
    DictBinTree.insert(dictionary,int(float(line))) #indsæt input i dictionary
    n = n+1

print() #start med tom linje
liste = DictBinTree.orderedTraversal(dictionary) #returner sorteret liste af input
i = 0
while i < n:
    print(liste[i]) #print listens elementer enkeltvist
    i = i+1
