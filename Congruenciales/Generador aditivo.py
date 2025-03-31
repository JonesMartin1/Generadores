def generador_congruencial_aditivo(semillas, m, n):
    """
    Método Congruencial Aditivo:
    Fórmula: X_n = (X_{n-1} + X_{n-k}) mod m

    Recomendaciones:
    - Semillas: una lista inicial de k valores (> 0 y < m).
    - m debe ser un entero grande aceptado por la máquina (ej: 2**31 - 1).
    
    Retorna:
    - Lista de números pseudoaleatorios
    """

    k = len(seeds := list(seeds := semillas))
    if n < k:
        raise ValueError("n debe ser mayor o igual que la cantidad de semillas.")

    for i in range(k, n):
        nuevo = (seeds[i - 1] + seeds[i - k]) % m
        seeds.append(nuevo)

    return [x for x in seeds[:n]]

# Ejemplo
if __name__ == "__main__":
    semillas = [?, ?, ?, ?, ?]  # mínimo 2 semillas, preferible más
    m = ?
    n = ? # Cantidad de números a generar

    nums = generador_congruencial_aditivo(semillas, m, n)
    for i, num in enumerate(nums, 1):
        print(f"{i}: {num}")
