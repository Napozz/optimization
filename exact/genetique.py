import gloutonOpti, random

class generation:
    def __init__(self, probleme):
        self.population = [gloutonOpti.glouton(alea=True) for _ in range(200)]
        self.probleme = probleme

    def croisement(self, individu1, individu2):
        r = random.randrange(len(individu1))
        return individu1[:r] + individu2[r:], individu2[:r] + individu1[r:]

    def mutation(self, individu, M):
        for u in range(individu):
            if random.randrange(len(individu)/2) == 0:
                individu[u] = random.randrange(M)
        return individu
    
    def reparation(self, individu, M, t):

        # # Recréation des chalets
        # chalets = []
        # for chalet in range(M):
        #     chalets.append([i for i in individu if i == chalet])
        
        # surpopulation = []
        # for i in range(M):
        #     if len(chalets[i]) > t[i]:
        #         surpopulation.append(chalets[i][t[i]-1:])
        #         chalets[i] = chalets[i][:t[i]-1]
        return self.adoption(individu)
        
    def adoption(self, individu):
        return gloutonOpti.glouton()
    
    def score(self):
        scores = [sum([self.probleme.couts[j-1] for j in set(i)]) for i in self.population]
        return scores

    def select(self, t):
        return sorted(self.population, key=self.score())