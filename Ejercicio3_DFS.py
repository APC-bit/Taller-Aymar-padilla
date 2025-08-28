

from collections import defaultdict

class GrafoLista:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_vertice(self, v):
        if v not in self.grafo:
            self.grafo[v] = []

    def agregar_arista(self, v1, v2):
        self.grafo[v1].append(v2)
        self.grafo[v2].append(v1)  # Grafo no dirigido


class GrafoDFS(GrafoLista):
    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        print(inicio, end=" ")
        for vecino in self.grafo[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)


# Prueba Ejercicio 3
if __name__ == "__main__":
    print("=== Ejercicio 3: DFS ===")
    g3 = GrafoDFS()
    for v in ["A","B","C","D"]:
        g3.agregar_vertice(v)
    g3.agregar_arista("A","B")
    g3.agregar_arista("A","C")
    g3.agregar_arista("B","D")

    print("Recorrido DFS desde A:")
    g3.dfs("A")
