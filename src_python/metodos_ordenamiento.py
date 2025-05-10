class MetodosOrdenamiento:
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def sortByBubbleMejorado(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    swapped = True
            if not swapped:
                break
        return arreglo

    def sort_selecction(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n - 1):
            minIndex = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[minIndex]:
                    minIndex = j
            arreglo[minIndex], arreglo[i] = arreglo[i], arreglo[minIndex]
        return arreglo

    def sortByInsercion(self, arreglo):
        arreglo = arreglo.copy()
        for i in range(1, len(arreglo)):
            clave = arreglo[i]
            j = i - 1
            while j >= 0 and clave < arreglo[j]:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = clave
        return arreglo

    def sortByShell(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo