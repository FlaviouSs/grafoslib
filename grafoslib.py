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

        if aux == 3:
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
                


class Aresta:

    def __init__(self, vertice1, vertice2, peso=None):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso

