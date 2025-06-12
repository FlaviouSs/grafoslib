class Grafo:

    def __init__(self):
        self.numeroVertices = 0
        self.numeroAresta = 0
        self.vertices = set()
        self.arestas = []
        self.flag_peso = False
        self.indexes_vertices = dict()
        self.lista_ajacencia = []
        self.matriz_adjacencia = None

    def processar_input(self, filepath):
        
        curret_free_index = 0

        with open(filepath, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        self.numeroVertices = int(lines[0])
        lines.pop(0)

        aux = lines[0].split()

        if len(aux) == 3:
            self.flag_peso = True
        
        if self.flag_peso:
            
            for line in lines:
                vertice1, vertice2, peso = line.split()
                
                vertice1 = int(vertice1)
                vertice2 = int(vertice2)
                peso = float(peso)
                
                self.vertices.add(vertice1)
                self.vertices.add(vertice2)
                self.numeroAresta += 1
                
                if(vertice1 not in self.indexes_vertices.values()):
                    self.indexes_vertices[curret_free_index] = vertice1
                    curret_free_index += 1
                if(vertice2 not in self.indexes_vertices.values()):
                    self.indexes_vertices[curret_free_index] = vertice2
                    curret_free_index += 1

                self.arestas.append(Aresta(vertice1, vertice2, peso))

        else:
                for line in lines:
                    vertice1, vertice2 = line.split()

                    vertice1 = int(vertice1)
                    vertice2 = int(vertice2)
                    
                    self.vertices.add(vertice1)
                    self.vertices.add(vertice2)
                    self.numeroAresta += 1

                    if(vertice1 not in self.indexes_vertices.values()):
                        self.indexes_vertices[curret_free_index] = vertice1
                        curret_free_index += 1
                    if(vertice2 not in self.indexes_vertices.values()):
                        self.indexes_vertices[curret_free_index] = vertice2
                        curret_free_index += 1

                    self.arestas.append(Aresta(vertice1, vertice2))
                

    def mapear_grau_dos_vertices(self):
        vertices = sorted(self.vertices)
        mapeamento_graus = dict()

        for v in vertices:
            mapeamento_graus[v] = 0 

        for v in vertices:
            for a in self.arestas:
                if (v == a.vertice1 or v == a.vertice2) and (a.vertice1 != a.vertice2):
                    mapeamento_graus[v] += 1
        
        return mapeamento_graus
    
    def calcular_grau_medio(self):
        return (2 * self.numeroAresta) / self.numeroVertices
    
    def distribuicao_empirica_graus(self):
        mapeamento = self.mapear_grau_dos_vertices()
        graus = set()
        distribuicao = dict()
        
        for _ in mapeamento.values():
            graus.add(_)

        grau_min = min(graus)
        grau_max = max(graus)

        for _ in range(grau_min, grau_max + 1):
            distribuicao[_] = 0

        for grau in graus:
            for v in mapeamento.keys():
                if grau == mapeamento[v]:
                    distribuicao[grau] += 1

        for _ in distribuicao.keys():
            distribuicao[_] = distribuicao[_] / self.numeroVertices

        return distribuicao

    def processar_output(self, filename):
        with open(filename, 'w') as f:
            f.write(f"# n = {self.numeroVertices}\n")
            f.write(f"# m = {self.numeroAresta}\n")
            f.write(f"# d_medio = {self.calcular_grau_medio()}\n")

            dist = self.distribuicao_empirica_graus()

            for _ in dist.keys():
                if(dist[_] != 0.0):
                    f.write(f"{_} {dist[_]:.2f}\n")
                else:
                    f.write(f"{_} 0\n")

class Aresta:

    def __init__(self, vertice1, vertice2, peso=None):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso

    def __str__(self):
        return f"{self.vertice1} - {self.vertice2} (peso:{self.peso})"

    def __repr__(self):
        return self.__str__()