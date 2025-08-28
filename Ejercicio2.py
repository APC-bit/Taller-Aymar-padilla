

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

    def mostrar(self):
        for v in self.grafo:
            print(v, "->", self.grafo[v])


# Prueba Ejercicio 2
if __name__ == "__main__":
    print("=== Ejercicio 2: Lista de Adyacencia ===")
    g2 = GrafoLista()
    for v in ["A","B","C","D"]:
        g2.agregar_vertice(v)
    g2.agregar_arista("A","B")
    g2.agregar_arista("A","C")
    g2.agregar_arista("B","D")
    g2.mostrar()
