import sys
sys.path.append("../exact")
import os
from GenerateLP import generateLP

"""
Ce programme permet de lancer la génération de tous les fichiers lp de toutes les instances,
ainsi que la commande glpsol sur chacun des fichiers .lp
"""
if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage : python3 glpk.py temps(en minutes)")
        # temps : temps maximum pour chaque commande glpk lancée
        sys.exit(0)

    categories = ["small", "large"]
    for categorie in categories:
        # Générer toutes les instances de la catégorie en format lp :
        cmd = f"ls -l ../instances/{categorie}/ > instances_names_{categorie}.txt"
        os.system(cmd)
        names_file = open(f"./instances_names_{categorie}.txt", "r")
        lines = names_file.readlines()
        lines_str = []
        for i in range(1, len(lines)):
            lines_str.append(lines[i].split())
        instances = []
        for i in range(len(lines_str)):
            instance = lines_str[i][len(lines_str[i])-1][:-4]
            print(f"{instance}.lp")
            instances.append(instance)
            generateLP(f"../instances/{categorie}/{instance}.txt", instance, categorie)


        # Générer la solution de chaque instance de la catégorie:
        for instance in instances:
            cmd = f"timeout --preserve-status {sys.argv[1]}m glpsol --lp ./instances/{categorie}/{instance}.lp --output ./solutions/{categorie}/solution.{instance}.txt"
            print(f"\nRésolution {instance}")
            if os.system(cmd) != 0:
                print(f"Command timeout for {instance}\nL'instance suivante ne sera pas résolue car elle a de grandes chances de nécessiter plus de temps de calculs.")
                #exit()
        
        # Suppression des fichiers listant les instances
        cmd = f"rm ./instances_names_{categorie}.txt"
        os.system(cmd)
            

    

    
