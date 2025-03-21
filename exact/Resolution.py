class Probleme:
    def __init__(self):
        self.M = 0 # Nombre de chalets
        self.N = 0 # Nombre d'étudiants à loger
        self.couts = [] # Couts des chalets
        self.capacites = [] # Capacités des chalets
        self.matrice = [] # Matrice de "qui s'entend avec qui", matrice carrée N

    def __str__(self):
        return f"M={self.M}\nN={self.N}\ncouts={self.couts}\nlen(couts)={len(self.couts)}\ncapacites={self.capacites}\nlen(capacites)={len(self.capacites)}\nmatrice=\n"+'\n'.join(str(self.matrice[i]) for i in range(self.N))

    def load(self, filename):
        try:
            file = open(filename, "r")
        except:
            return False
        lignes = file.readlines()
        file.close()

        # Récupération de M et N sur la première ligne du fichier :
        self.M, self.N = int(lignes[0].split()[0]), int(lignes[0].split()[1])

        # Récupérations des coûts et des capacités des chalets. Coût : colonne de gauche, capacité : colonne de droite.
        for i in range(self.M):
            self.couts.append(int(lignes[i+1].split()[0]))
            self.capacites.append(int(lignes[i+1].split()[1]))

        # Matrice de "qui s'entend avec qui" :
        debut = 1 + self.M #ligne 1 + lignes des coûts et capacités

        # Initialisation de la matrice carrée N :
        for i in range(self.N):
            row = []
            self.matrice.append(row)
            for j in range(self.N):
                row.append(0)

        # Remplissage de la matrice :
        for i in range(self.N):
            nbpma =  int(lignes[i+debut].split()[0]) # nbpma = nombre de personnes mal aimées
            for l in range(nbpma): # Pour l allant de 0 au nombre de personnes avec qui i ne s'entend pas
                num_pma = int(lignes[i+debut].split()[l+1]) # num_pma = numéro de la personne mal aimée par i
                self.matrice[i][num_pma]=1 # on met un 1 la valeur de l'indice num_pma ième de la liste des personnes que i n'aime pas
            

        # Parcours de la matrice pour la rendre symétrique :
        for i in range(self.N):
            for j in range(self.N):
                self.matrice[j][i]=self.matrice[i][j]

        # Affichage test de la matrice :
        #for i in range(self.N):
        #    print(f"{self.matrice[i]}")

        return self