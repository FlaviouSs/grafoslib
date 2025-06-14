import grafoslib

g = grafoslib.Grafo()

g.processar_input("./input1.txt")

g.gerar_lista_adjacencia()

#print(g.lista_ajacencia)

g.gerar_matriz_adjacencia()

#print(g.matriz_adjacencia)

g.DFS_por_lista(1, "./output1.txt")
g.DFS_por_matriz(1, "./output2.txt")
g.BFS_por_lista(1,"./output3.txt")
g.BFS_por_matriz(1, "./output4.txt")
