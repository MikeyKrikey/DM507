'''
Gruppe:

Stine Holz Meinhardt Gregersen, sgreg18
Michael Kristensen, mickr19
Hanna Bruun-Schmidt, habru19

'''

# Program skal implementere datastrukturen binært søgetræ med tal som nøgler


# Vores implementering af search
# Skal returnere en boolean, der angiver om nøglen k er i træet T.
def search(T,k):
    if T[0] == None:
        return False
    if k == T[0][0]:
        return True
    if k < T[0][0]:
        return search([T[0][1]], k) #rekursivt, kigger på venstre undertræ
    else:
        return search([T[0][2]], k) #rekursivt kigger på højre undertræ
    


# vores implementering af insert
# indsætter nøglen k i træet T.
def insert(T,k):
    y = None 
    k = [k, None, None] #lad nøglen k være en knude med to tomme undertræer
    x = T[0]
    while x != None:
        y = x
        if k[0] < x[0]:
            x = x[1] #hvis nøglen er mindre end x, så kig på venstre undertræ
        else: 
            x = x[2] #hvis nøglen er større end x, så kig på højre undertræ
    if y == None:
        T[0] = k #indsæt k som rod, hvis træet er tomt
    elif k[0] < y[0]:
        y[1] = k #indsæt k til venstre for bladet y, hvis mindre
    else:
        y[2] = k #indsæt k til højre for bladet y, hvis større
    
    



# vores implementering af inorder gennemløb (Træet skal ikke holdes balanceret)
# returnerer en liste med nøglerne i træet T i sorteret orden (fremfor at printe dem på skærmen som i bogens pseudo-kode)
def orderedTraversal(T, liste = []):
    if T[0] != None:
        orderedTraversal([T[0][1]], liste) #rekursivt, kig på venstre undertræ efter mindste element
        liste.append(T[0][0]) #indsæt element i liste
        orderedTraversal([T[0][2]], liste) #rekursivt kig på højre undertræ efter mindste element
    return liste
    

# returnerer et nyt tomt træ
def createEmptyDict():
    return [None]


