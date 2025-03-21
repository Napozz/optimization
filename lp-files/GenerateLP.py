import sys
sys.path.append("../exact")
from Resolution import Probleme

def generateLP(instance, name, categorie):

    if(categorie == "small" or categorie == "large"):
        # Créer un objet Probleme 
        probleme = Probleme()
        probleme_loaded = probleme.load(instance)

        # Ecriture de l'objectif :
        # Somme pour k allant de 1 à M de c_k * x_k
        objectif = "z: "
        for k in range(probleme_loaded.M):
            objectif = objectif+f"{probleme_loaded.couts[k]} x{k+1}"
            if k != probleme_loaded.M-1:
                objectif +=" + "

        # Ecriture des contraintes :
        contraintes = ""
        # Contrainte A
        # Contrainte de relation entre X et Y
        for i in range(probleme_loaded.N):
            for k in range(probleme_loaded.M):
                a = ""
                a += f"a{i+1}a{k+1}: y{i+1},{k+1} - x{k+1} <= 0\n"
                contraintes += a
        
        #Contrainte B
        # Contrainte d'entente entre deux étudiants i et j
        for i in range(probleme_loaded.N):
            for j in range(probleme_loaded.N):
                b = ""
                if j != i and probleme_loaded.matrice[i][j] == 1 :
                    for k in range(probleme_loaded.M):
                        b += f"b{i+1}b{j+1}b{k+1}: y{i+1},{k+1} + y{j+1},{k+1} <= 1\n"
                    contraintes += b

        # Contrainte C
        # Contrainte d'existence, le fait d'affecter l'étudiant i à un et un seul chalet k
        for i in range(probleme_loaded.N):
            c = ""
            c += f"c{i+1}: "
            for k in range(probleme_loaded.M):
                if k == probleme_loaded.M-1:
                    c += f"y{i+1},{k+1}"
                else : c += f"y{i+1},{k+1} + "
            c += " = 1\n"
            contraintes += c

        # Contrainte D
        # Contrainte de capacité des chalets
        for k in range(probleme_loaded.M):
            d = ""
            d += f"d{k+1}: "
            for i in range(probleme_loaded.N):
                if i == probleme_loaded.N-1:
                    d += f"y{i+1},{k+1}"
                else : d += f"y{i+1},{k+1} + "
            d += f" <= {probleme_loaded.capacites[k]}\n"
            contraintes += d

        variables = ""
        for k in range(probleme_loaded.M):
            variables += f"x{k+1}\n"
        for k in range(probleme_loaded.M):
            for i in range(probleme_loaded.N):
                if k == probleme_loaded.M-1 and i == probleme_loaded.N-1:
                    variables += f"y{k+1},{i+1}"
                else : variables += f"y{k+1},{i+1}\n"

        lp_file = open(f"./instances/{categorie}/{name}.lp", "x")
        fichier = f"Minimize\n{objectif}\nSubject To\n{contraintes}Binaries\n{variables}\nEnd"
        lp_file.write(fichier)
    else :
        print("erreur catégorie des instances")
        return 0