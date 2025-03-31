def generador_congruencial_multiplicativo(semilla, a, m, n):
    """
    Método Congruencial Multiplicativo:
    Fórmula: X_{n+1} = (a * X_n) mod m

    Recomendaciones:
    - a debe ser impar, no divisible por 3 ni por 5.
    - m debe ser el número entero más grande que la computadora acepte.
    - X0 (semilla) debe ser mayor a 0 (si es 0, la secuencia se estanca).
    
    Retorna:
    - Lista de números pseudoaleatorios
    """

    if semilla == 0:
        raise ValueError("La semilla no puede ser 0 en el método multiplicativo.")

    numeros = []
    x = semilla
    for _ in range(n):
        x = (a * x) % m
        numeros.append(x)
    return numeros

# Ejemplo
if __name__ == "__main__":
    semilla = ?
    a = ?
    m = ?
    n = ? # Cantidad de números a generar

    nums = generador_congruencial_multiplicativo(semilla, a, m, n)
    for i, num in enumerate(nums, 1):
        print(f"{i}: {num}")
