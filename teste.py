import grafoslib

g = grafoslib.Grafo()

g.processar_input("grafoslib/input1.txt")

g.gerar_lista_adjacencia()

#print(g.lista_ajacencia)

g.gerar_matriz_adjacencia()

#print(g.matriz_adjacencia)

x = g.DFS_por_lista(4)
y = g.DFS_por_matriz(4)

print(x)
print(y)
