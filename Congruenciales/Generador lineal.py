def generador_congruencial_mixto(semilla, a, c, m, n):
    """
    Método Congruencial Mixto:
    Fórmula: X_{n+1} = (a * X_n + c) mod m

    Recomendaciones:
    - a debe ser un número impar, no divisible por 3 ni por 5.
    - c debe ser menor que m, positivo, y no tener factores primos en común con m (excepto el 1).
    - m debe ser el número entero más grande que la computadora acepte (por ejemplo, 2**31 - 1 en muchos casos).
    
    Retorna:
    - Lista de números pseudoaleatorios
    """

    numeros = []
    x = semilla
    for _ in range(n):
        x = (a * x + c) % m
        numeros.append(x)
    return numeros

# Ejemplo
if __name__ == "__main__":
    semilla = ?
    a = ?
    c = ?
    m = ?
    n = ? # Cantidad de números a generar

    nums = generador_congruencial_mixto(semilla, a, c, m, n)
    for i, num in enumerate(nums, 1):
        print(f"{i}: {num}")
