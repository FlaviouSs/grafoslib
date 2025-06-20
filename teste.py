import grafoslib

# 1.    Primeiro, o usuário deve instânciar a classe Grafo()
g = grafoslib.Grafo()

# 2.    O arquivo de input deve ser processado
g.processar_input("./input1.txt")

# 3.    A representação do grafo a ser utilizada é escolhida
g.gerar_lista_adjacencia()
g.gerar_matriz_adjacencia()


# 4.    A lógica desejada é implementada
g.DFS_por_lista(1, "./output1.txt")
g.DFS_por_matriz(1, "./output2.txt")
g.BFS_por_lista(1,"./output3.txt")
g.BFS_por_matriz(1, "./output4.txt")

#g.encontrar_componentes_conexos()

# PARTE 2
print()
distancias, caminhos = g.menor_caminho(origem=1, destino=2)

print(distancias)
print(caminhos)
