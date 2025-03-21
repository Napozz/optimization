from Resolution import Probleme
import sys, random

tabEDC = []
tabCDC = []

def calculscore(chalets, pb):
    score = 0
    print("calcul: ", chalets)
    for i in range(len(chalets)):
        if len(chalets[i]) != 0:
            score = score + pb.couts[i]
    
    print(score)

def chaletSorted(cR, nChalet):
    cR.sort(key=takeSecond)
    n = 0
    while n < nChalet:
        if cR[n] in tabCDC:
            n+=1
        else:
            return cR[n]
    return [0,0]
    
    
def takeSecond(elem):
    return elem[1]

def choixEtudiant(matrice):
    max = 0
    r = 0
    
    for i in range(len(matrice)):
        s = sum(matrice[i])
        if s > max and not (i in tabEDC) :
            max = s 
            r = i
    tabEDC.append(r)
    return r

def choixEtudiantRandom(matrice):
    
    i = random.randrange(len(matrice))
    while i in tabEDC:
        i = random.randrange(len(matrice))
    tabEDC.append(i)
    return i

def choixChalet(e, c ,cR ,pb):
    chalet = []
    chaletPotentiel = []
    if len(tabCDC) == 0:
        chalet = cR.index(min(cR, key=takeSecond))
        tabCDC.append(min(cR, key=takeSecond))
        return chalet
    else:
        for i in range(pb.M):
            if len(c[i]) < pb.capacites[i] and len(c[i]) != 0:
                ennemi = -1
                for m in c[i]:
                    if ennemi <= 0:
                        if pb.matrice[e][m] == 1:
                            ennemi = 1
                        else:
                            ennemi = 0
                if ennemi == 0:
                    chaletPotentiel.append(i)
                    
    if chaletPotentiel == []:
        cP = chaletSorted(cR, pb.M)               
        tabCDC.append(cP)
        chaletPotentiel.append(cP[0])
    less = 10000
    for k in chaletPotentiel:
            if (cR[k][1] < less):
                less = cR[k][1]
                chalet = k
    return chalet

def glouton(alea:bool = False):
    if len(sys.argv)!=2: #mettre 3 pour ajouter le mode
        print("Usage : python3 main.py instance") #sans mode
        #print("Usage : python3 main.py instance mode")
        sys.exit(0)
    probleme = Probleme()
    if not probleme.load(sys.argv[1]):
        print(f"Impossible de charger {sys.argv[1]}")
        sys.exit(0)
    
    print(probleme)
    
    nbEtudiantRestant = probleme.N
    chalets = []
    chaletsRentable = []
    for i in range(probleme.M):
        chalets.append([])
        value = probleme.couts[i] // probleme.capacites[i]
        chaletsRentable.append([i, value])
        
    
        
    while nbEtudiantRestant > 0:
        if alea:
            etudiant = choixEtudiantRandom(probleme.matrice)
        else:
            etudiant = choixEtudiant(probleme.matrice)
        chalet = choixChalet(etudiant, chalets,chaletsRentable, probleme)
        chalets[chalet].append(etudiant)
        nbEtudiantRestant-=1

    return [n + 1 for i in range(probleme.N) for n, j in enumerate(chalets) if i in j]

if __name__ == '__main__':
        
    print(glouton())
    
    print(chalets)
    
    calculscore(chalets, probleme)
        
    
