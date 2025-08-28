
class GrafoMatriz:
    def __init__(self):
        self.vertices = []
        self.matriz = []

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            n = len(self.vertices)
            for fila in self.matriz:
                fila.append(0)
            self.matriz.append([0]*n)

    def agregar_arista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i, j = self.vertices.index(v1), self.vertices.index(v2)
            self.matriz[i][j] = 1
            self.matriz[j][i] = 1    # Grafo no dirigido

    def mostrar(self):
        print("   " + " ".join(self.vertices))
        for i, fila in enumerate(self.matriz):
            print(self.vertices[i], fila)


# Prueba Ejercicio 1
if __name__ == "__main__":
    print("=== Ejercicio 1: Matriz de Adyacencia ===")
    g = GrafoMatriz()
    for v in ["A","B","C","D"]:
        g.agregar_vertice(v)
    g.agregar_arista("A","B")
    g.agregar_arista("B","C")
    g.agregar_arista("C","D")
    g.agregar_arista("D","A")
    g.mostrar()
