import matplotlib.pyplot as plt

class Grafica:
    def __init__(self, tamanios, resultados):
        self.tamanios = tamanios
        self.resultados = resultados  # lista de tuplas (tam, nombre_algoritmo, tiempo)

    def generar_grafica(self, titulo="Comparación de algoritmos de Ordenamiento", autor="Pedro Pesántez - Jonnathan Saavedra"):
        tiempos_by_metodo = {}
        for tam, nombre, tiempo in self.resultados:
            if nombre not in tiempos_by_metodo:
                tiempos_by_metodo[nombre] = []
            tiempos_by_metodo[nombre].append(tiempo)

        fig = plt.figure(figsize=(12, 6))
        for nombre, tiempos in tiempos_by_metodo.items():
            plt.plot(self.tamanios, tiempos, label=nombre, marker='o')

        plt.grid()
        plt.legend()
        plt.title(f"{titulo}\n{autor}")
        fig.canvas.manager.set_window_title(f"{autor}")
        plt.xlabel("Tamaño del arreglo")
        plt.ylabel("Tiempo de ejecución (s)")
        plt.tight_layout()
        plt.show()