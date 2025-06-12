import grafoslib

g = grafoslib.Grafo()

g.processar_input('./input2.txt')

print(g.numeroVertices)
print(g.vertices)
print(g.indexes_vertices)
print(g.arestas)