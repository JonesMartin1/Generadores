def generador_combinacion_lineal(semilla1, a1, c1, m1,
                                  semilla2, a2, c2, m2, n):
    """
    Método de Combinación Lineal de dos generadores congruenciales mixtos.
    
    Fórmula:
        X_n = (X_n^(1) - X_n^(2)) mod m1

    Recomendaciones:
    - a debe ser impar, no divisible por 3 ni 5.
    - c debe ser positivo, menor que m y coprimo con m.
    - m1 y m2 deben ser grandes (ej. 2**31 - 1) y preferentemente primos.
    - Ideal para mejorar la calidad estadística del generador.
    
    Parámetros:
    - semilla1, a1, c1, m1: parámetros del primer generador
    - semilla2, a2, c2, m2: parámetros del segundo generador
    - n: cantidad de números a generar

    Retorna:
    - Lista de números pseudoaleatorios 
    """
    x1 = semilla1
    x2 = semilla2
    resultados = []

    for _ in range(n):
        x1 = (a1 * x1 + c1) % m1
        x2 = (a2 * x2 + c2) % m2
        combinado = (x1 - x2) % m1
        resultados.append(combinado)  # Normalización en [0, 1)
    
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    # Generador 1
    semilla1 = ?
    a1 = ?
    c1 = ?
    m1 = ?

    # Generador 2
    semilla2 = ?
    a2 = ?
    c2 = ?
    m2 = ?

    n = ? # Cantidad de números a generar

    numeros = generador_combinacion_lineal(
        semilla1, a1, c1, m1,
        semilla2, a2, c2, m2,
        n
    )

    for i, num in enumerate(numeros, 1):
        print(f"{i}: {num}")
