import grafoslib

g = grafoslib.Grafo()

g.processar_input('./input1.txt')

g.gerar_lista_adjacencia()

g.DFS_por_lista(3)
print()
g.gerar_matriz_adjacencia()
print()
g.DFS_por_matriz(3)