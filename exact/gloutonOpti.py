from Resolution import Probleme
import sys, random

tabEDC = [] # Liste des Etudiants Déjà Choisis
tabCDC = [] # Liste des Chalets Déjà Choisis
def calculscore(chalets, pb):
    score = 0
    for i in range(len(chalets)):
        if len(chalets[i]) != 0:
            score = score + pb.couts[i]
    return score

def chaletSorted(cR, nChalet): # cR = chalet Rentable
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

def takeThird(elem):
    return elem[2]

def choixEtudiant(matrice):
    max = 0
    r = 0
    
    for i in range(len(matrice)):
        s = sum(matrice[i]) # Nombre d'ennemis de l'étudiant i
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

def choixChalet(etudiant, c ,cR ,pb):
    chalet_choisi : int = -1
    chalet_potentiel = []
    # Cas où on n'a pas encore choisi un seul chalet :
    if len(tabCDC) == 0:
        chalet_choisi = cR.index(min(cR, key=takeSecond))
        tabCDC.append(min(cR, key=takeSecond))
        return chalet_choisi
    # Cas où un ou plusieurs chalet(s) ont déjà été choisis :
    else:
        for k in range(pb.M):
            if len(c[k]) < pb.capacites[k] and len(c[k]) != 0:
                ennemi = -1
                for m in c[k]:
                    if ennemi <= 0:
                        if pb.matrice[etudiant][m] == 1:
                            ennemi = 1
                        else:
                            ennemi = 0
                if ennemi == 0:
                    chalet_potentiel.append(k)
                    
    if chalet_potentiel == []:
        cP = chaletSorted(cR, pb.M)               
        tabCDC.append(cP)
        chalet_potentiel.append(cP[0])
    less = 10000
    for k in chalet_potentiel:
            if (cR[k][1] < less):
                less = cR[k][1]
                chalet_choisi = k
    return chalet_choisi


def opimiserSolution(chalets, pb):
    # print(pb)
    # print(chalets)
    temp = []
    format = []
    for i in range(pb.M):
        if len(chalets[i]) != 0:
            temp.append([i, len(chalets[i]),pb.couts[i], pb.capacites[i]])
            
        format.append([i, len(chalets[i]),pb.couts[i], pb.capacites[i]])
        
    temp = sorted(temp, key=takeThird, reverse=True)
    
    # print(temp)
    for i in temp:
        idx = i[0]
        select = 10000
        for j in format:
            if j[2] < i[2] and j[3] >= i[1] and j[1] == 0 and j[2] < select:
                idx = j[0]
                select = j[2]
            
        chalets[idx] = chalets[i[0]]
        format[idx][1]=len(chalets[idx])
        format[i[0]][1] = 0
        if idx != i[0]:
            chalets[i[0]] = []
    
    return [n + 1 for i in range(pb.N) for n, j in enumerate(chalets) if i in j]
    
def glouton(alea:bool = False):

    if len(sys.argv)!=2: #mettre 3 pour ajouter le mode
        print("Usage : python3 main.py instance") #sans mode
        #print("Usage : python3 main.py instance mode")
        sys.exit(0)
    probleme = Probleme()
    if not probleme.load(sys.argv[1]):
        print(f"Impossible de charger {sys.argv[1]}")
        sys.exit(0)
    
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
        
    
    
    solution = opimiserSolution(chalets, probleme)
    
    score = calculscore(chalets, probleme)
    return solution, score
    
if __name__ == '__main__':

    print(glouton())