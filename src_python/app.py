from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
from grafica import Grafica

if __name__ == "__main__":
    tamanios = [5000, 10000, 30000, 50000, 100000]
    benchmark = Benchmarking()
    metodosOrden = MetodosOrdenamiento()

    resultados = []
    arreglo_maestro = benchmark.build_arreglo(tamanios[-1])

    metodos = {
        "burbuja": metodosOrden.sortByBubble,
        "burbujaMejorado": metodosOrden.sortByBubbleMejorado,
        "seleccion": metodosOrden.sort_selecction,
        "insercion": metodosOrden.sortByInsercion,
        "shell": metodosOrden.sortByShell
    }

    for tam in tamanios:
        arreglo_base = arreglo_maestro[:tam]  # Subconjunto del arreglo más grande
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo))
            print(f"Tamano: {tam}, Algoritmo: {nombre}, Tiempo: {tiempo:.6f} segundos")

    grafica = Grafica(tamanios, resultados)
    grafica.generar_grafica()