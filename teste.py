import grafoslib

g = grafoslib.Grafo()

g.processar_input('./input1.txt')

g.gerar_lista_adjacencia()

g.BFS_por_lista(1)

g.gerar_matriz_adjacencia()

print()

g.BFS_por_matriz(1)
