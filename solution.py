# JUAN CAMILO SILVA - 2122913
# LESLI ESMITH MARTINEZ - 2126928
# JOSE ANTONIO TUMIÑA - 2077419


def merge_sort(arr):
    """Función que implementa Merge Sort."""
    if len(arr) <= 1:
        return arr  # Caso base: si la lista tiene un solo elemento o está vacía, está ordenada.
    
    mid = len(arr) // 2  # Divide la lista en dos mitades.
    left = merge_sort(arr[:mid])  # Llama recursivamente a merge_sort en la mitad izquierda.
    right = merge_sort(arr[mid:])  # Llama recursivamente a merge_sort en la mitad derecha.
    
    return merge(left, right)  # Combina las dos mitades ordenadas.

def merge(left, right):
    """Combina dos sublistas ordenadas."""
    result = []  # Lista para almacenar el resultado combinado.
    i = j = 0  # Índices para recorrer las sublistas izquierda y derecha.
    
    while i < len(left) and j < len(right):  # Compara elementos de ambas sublistas.
        if left[i][0] <= right[j][0]:  # Compara los primeros elementos de las tuplas.
            result.append(left[i])  # Añade el elemento menor a la lista resultante.
            i += 1  # Avanza en la lista izquierda.
        else:
            result.append(right[j])  # Añade el elemento de la derecha si es menor.
            j += 1  # Avanza en la lista derecha.
    
    result.extend(left[i:])  # Añade los elementos restantes de la izquierda.
    result.extend(right[j:])  # Añade los elementos restantes de la derecha.
    
    return result  # Devuelve la lista combinada y ordenada.

def process_intervals(n, k, intervals):
    """Procesa los intervalos y determina si es posible cocinar la hamburguesa correctamente."""
    intervals = merge_sort(intervals)  # Ordena los intervalos por el tiempo de inicio.
    flips = 0
    current_time = 0  # Tiempo cocinado en un lado.
    total_cooking_time = 0  # Tiempo total cocinado en ambos lados.

    for (li, ri) in intervals:
        # Si el intervalo se solapa con el tiempo actual de cocción, sumar el tiempo.
        if li < current_time:
            # Si hay solapamiento, solo contamos el tiempo adicional en este intervalo.
            total_cooking_time += ri - current_time
        elif li >= current_time:
            # Si no hay solapamiento, simplemente cocinamos desde el inicio del intervalo.
            total_cooking_time += ri - li
        
        # Cada vez que el tiempo de cocción acumulado alcanza el tiempo necesario por lado, lo registramos.
        if total_cooking_time >= 2 * n:
            flips += 1
            current_time += n  # Volteamos la hamburguesa, y sumamos el tiempo n a la cocción total.
            total_cooking_time = 0  # Reiniciamos el tiempo de cocción para el siguiente lado.

        # Si ya se ha cocinado completamente (2 * n tiempo), salimos y mostramos el resultado.
        if current_time >= 2 * n:
            return f"Perfect burger!\n{flips}"

    # Si no se alcanzó el tiempo necesario de cocción, la hamburguesa no está perfecta.
    return "Another bland and poorly cooked burger!" if current_time < 2 * n else None

def main():
    with open('B.in', 'r') as file_in:
        c = int(file_in.readline())  # Lee el número de casos de prueba.
        results = []  # Almacena los resultados de cada caso.
        
        for _ in range(c):
            n, k = map(int, file_in.readline().split())  # Lee n (tiempo por lado) y k (número de intervalos).
            intervals = [tuple(map(int, file_in.readline().split())) for _ in range(k)]  # Lee los intervalos.
            result = process_intervals(n, k, intervals)  # Procesa cada caso.
            results.append(result)
    
    # Comparar resultados con el archivo esperado B.out
    with open('B.out', 'r') as file_out:
        expected_output = file_out.read().strip().split("\n")
        
        for idx, (result, expected) in enumerate(zip(results, expected_output)):
            if result != expected:
                print(f"Discrepancia en la prueba {idx + 1}: Esperado '{expected}', obtenido '{result}'")
            else:
                print(result)  # Imprime el resultado correcto.

if __name__ == "__main__":
    main()
