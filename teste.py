import grafoslib

g = grafoslib.Grafo()

g.processar_input('./input1.txt')

print(g.numeroVertices)
print(g.vertices)
print(g.indexes_vertices)
print(g.arestas)
print(g.calcular_grau_medio())
print(g.mapear_grau_dos_vertices())
print(g.distribuicao_empirica_graus())


g.processar_output("./output1.txt")