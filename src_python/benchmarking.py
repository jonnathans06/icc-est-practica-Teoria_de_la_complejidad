import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print('Benchmarking inicializado')

    def build_arreglo(self, size):
        random.seed(42)  # Semilla para que siempre genere los mismos números
        return [random.randint(1, 100000) for _ in range(size)]

    def medir_tiempo(self, metodo, arreglo):
        inicio = time.perf_counter()
        metodo(arreglo.copy())
        fin = time.perf_counter()
        return fin - inicio