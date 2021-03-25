'''
Gruppe:

Stine Holz Meinhardt Gregersen, sgreg18
Michael Kristensen, mickr19
Hanna Bruun-Schmidt, habru19

'''

# Program skal implementere datastrukturen binært søgetræ med tal som nøgler

"""
p. 290 bogens pseudo-kode for tree-search.

Tree-Search(x,k)
    if x == NIL or k == x.key:
        return x
    if k < x.key:
        return Tree-Search(x.left, k)
    else:
        return Tree-Search(x.right,k)

eller p.291 iterative-tree-search

Iterative-Tree-Search(x,k)
    while x != NIL and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x
"""
# Vores implementering af search
def search(T,k):
    # Skal returnerer en boolean, der angiver om nøglen k er i træet T.

"""
p. 294 bogens pseudo-kode for tree-insert.

Tree-Insert(T,z)
    y = NIL 
    x = T.root

    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else: 
            x = x.right
    z.p = y

    if y == NIL:
        T.root = z // tree T was empty
    elseif z.key < y.key:
        y.left = z
    else:
        y.right = z
"""
# vores implementering af insert
def insert(T,k):
    # indsætter nøglen k i træet T.

"""
p. 288 bogens pseudo-kode af inorder-tree-walk

Inorder-Tree-Walk(x)
    if x != NIL:
        Inorder-Tree-Walk(x.left)
        print x.key
        Inorder-Tree-Walk(x.right)
"""

# vores implementering af inorder gennemløb (Træet skal ikke holdes balanceret)
def orderedTraversal(T):
    # returnerer en liste med nøglerne i træet T i sorteret orden (fremfor at printe dem på skærmen som i bogens pseudo-kode)

def createEmptyDict():
    # returnerer et nyt tomt træ
