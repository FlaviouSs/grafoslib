import grafoslib

g = grafoslib.Grafo()

g.processar_input('./input1.txt')

print(g.numeroVertices)
print(g.vertices)
print(g.arestas)

print(g.indexes_vertices)

g.processar_output("./output1.txt")