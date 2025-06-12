import grafoslib

g = grafoslib.Grafo()

g.processar_input('./input1.txt')

g.gerar_lista_adjacencia()

#print(g.lista_ajacencia)

g.gerar_matriz_adjacencia()

#print(g.matriz_adjacencia)

x = g.DFS_por_lista(3)
y = g.DFS_por_matriz(3)

print()
print()
print(x)
print(y)
print()
print()
k = g.encontrar_componentes_conexos()
print(k)