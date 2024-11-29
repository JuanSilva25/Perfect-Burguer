def merge_sort(arr):
    """Función que implementa Merge Sort."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Combina dos sublistas ordenadas."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def process_intervals(n, k, intervals):
    """Procesa los intervalos y determina si es posible cocinar la hamburguesa correctamente."""
    intervals = merge_sort(intervals)  # Ordena los intervalos por el tiempo de inicio.
    flips = 0
    current_time = 0  # Tiempo cocinado en un lado.

    for (li, ri) in intervals:
        if li <= current_time < ri:
            flips += 1
            current_time += n  # Agregamos tiempo n cada vez que volteamos
        if current_time >= 2 * n:
            return f"Perfect burger!\n{flips}"
    return "Another bland and poorly cooked burger!" if current_time < 2 * n else None

def main():
    with open('B.in', 'r') as file_in:
        c = int(file_in.readline())  # Número correcto de casos: 200 en este caso.
        results = []  # Para guardar los resultados
        for _ in range(c):
            n, k = map(int, file_in.readline().split())
            intervals = [tuple(map(int, file_in.readline().split())) for _ in range(k)]
            result = process_intervals(n, k, intervals)
            results.append(result)
    
    # Comparar resultados con archivo esperado B.out
    with open('B.out', 'r') as file_out:
        expected_output = file_out.read().strip().split("\n")
        for idx, (result, expected) in enumerate(zip(results, expected_output)):
            if result != expected:
                print(f"Discrepancia en la prueba {idx + 1}: Esperado '{expected}', obtenido '{result}'")
            else:
                print(result)

if __name__ == "__main__":
    main()
