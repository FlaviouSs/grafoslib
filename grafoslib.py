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

                self.arestas.append(Aresta(vertice1, vertice2, peso))

        else:
                for line in lines:
                    vertice1, vertice2 = line.split()

                    vertice1 = int(vertice1)
                    vertice2 = int(vertice2)
                    
                    self.vertices.add(vertice1)
                    self.vertices.add(vertice2)
                    self.numeroAresta += 1

                    self.arestas.append(Aresta(vertice1, vertice2))

        if(self.numeroVertices > len(self.vertices)):
            for i in range(max(self.vertices) + 1, self.numeroVertices + 1):
                self.vertices.add(i)


        for v in sorted(self.vertices):
            self.indexes_vertices[v] = curret_free_index
            curret_free_index += 1
                

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

    def gerar_lista_adjacencia(self):
        lista = []

        for _ in range(0, self.numeroVertices):
            lista.append([])

        for v in self.vertices:
            for a in self.arestas:
                if v == a.vertice1:
                    lista[self.indexes_vertices[v]].append((a.vertice2, a.peso))
                elif v == a.vertice2:
                    lista[self.indexes_vertices[v]].append((a.vertice1, a.peso))

        self.lista_ajacencia = lista

    def gerar_matriz_adjacencia(self):
        matriz = [[[] for _ in range(self.numeroVertices)] for _ in range(self.numeroVertices)]

        for v in self.vertices:
            for a in self.arestas:
                if v == a.vertice1:
                    matriz[self.indexes_vertices[v]][self.indexes_vertices[a.vertice2]].append((a.vertice1, a.vertice2, a.peso))
                elif v == a.vertice2:
                    matriz[self.indexes_vertices[v]][self.indexes_vertices[a.vertice1]].append((a.vertice1, a.vertice2, a.peso))
        
        self.matriz_adjacencia = matriz

    def __DFSUtil_lista(self, v, visitado, resultado):
        visitado.add(v)
        #print(v, end=" ")
        resultado.append(v)

        for vizinho in self.lista_ajacencia[self.indexes_vertices[v]]:
            if vizinho[0] not in visitado:
                self.__DFSUtil_lista(vizinho[0], visitado, resultado)

    def DFS_por_lista(self, v):
        visitado = set()
        resultado = []
        self.__DFSUtil_lista(v, visitado, resultado)
        return resultado

    def __DFSUtil_matriz(self, v, visitado, resultado):
        visitado.add(v)
        #print(v, end=" ")
        resultado.append(v)

        for vizinho in self.matriz_adjacencia[self.indexes_vertices[v]]:
            if len(vizinho) > 0:
                for tupla in vizinho:
                    if tupla[0] not in visitado:
                        self.__DFSUtil_matriz(tupla[0], visitado, resultado)
                    elif tupla[1] not in visitado:
                        self.__DFSUtil_matriz(tupla[1], visitado, resultado)
        


    def DFS_por_matriz(self, v):
        visitado = set()
        resultado = []
        self.__DFSUtil_matriz(v, visitado, resultado)
        return resultado

    def BFS_por_lista(self, v):
        visitado = set()
        fila = []
        resultado = []

        fila.append(v)
        visitado.add(v)

        while fila:
            v = fila.pop(0)
            #print(v, end=" ")
            resultado.append(v)

            for vizinho in self.lista_ajacencia[self.indexes_vertices[v]]:
                if vizinho[0] not in visitado:
                    fila.append(vizinho[0])
                    visitado.add(vizinho[0])
        
        return resultado
    
    def BFS_por_matriz(self, v):
        visitado = set()
        fila = []
        resultado = []

        fila.append(v)
        visitado.add(v)

        while fila:
            v = fila.pop(0)
            #print(v, end=" ")
            resultado.append(v)

            for vizinho in self.matriz_adjacencia[self.indexes_vertices[v]]:
                if len(vizinho) > 0:
                    for tupla in vizinho:
                        if tupla[0] not in visitado: 
                            fila.append(tupla[0])
                            visitado.add(tupla[0])
                        elif tupla[1] not in visitado:
                            fila.append(tupla[1])
                            visitado.add(tupla[1])
        
        return resultado

    def encontrar_componentes_conexos(self):
        
        self.gerar_lista_adjacencia()

        visitado = set()
        componentes = []
        for v in self.vertices:
            if v not in visitado:
                componente = sorted(self.BFS_por_lista(v))
                componentes.append(componente)
                visitado.update(componente)

        componentes.sort(key=len, reverse=True)

        return componentes

class Aresta:

    def __init__(self, vertice1, vertice2, peso=None):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso

    def __str__(self):
        return f"{self.vertice1} - {self.vertice2} (peso:{self.peso})"

    def __repr__(self):
        return self.__str__()