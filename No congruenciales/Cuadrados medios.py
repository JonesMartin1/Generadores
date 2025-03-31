def cuadrados_medios(semilla, n):
    """
    Método de los Cuadrados Medios de Von Neumann:
    Fórmula: 
        X_{n+1} = extraer_digitos_centrales((X_n)^2)

    Donde:
    - Se eleva al cuadrado la semilla actual.
    - Se extraen los dígitos centrales para formar el siguiente número.
    - Se normaliza el resultado dividiéndolo por 10^d para obtener un número en [0, 1).

    Recomendaciones:
    - La semilla debe tener un número par de dígitos (preferiblemente 4 o 6).
    - No debe ser 0000, ya que lleva a un ciclo muerto.
    - Este método es útil con pocas cifras; no recomendado para muchas generaciones

    Parámetros:
    - semilla: número inicial (entero, con longitud par de dígitos)
    - n: cantidad de números a generar

    Retorna:
    - Lista de números pseudoaleatorios
    """

    resultados = []
    x = semilla
    d = len(str(semilla))

    if d % 2 != 0:
        raise ValueError("La semilla debe tener un número par de dígitos.")

    for _ in range(n):
        cuadrado = str(x ** 2).zfill(2 * d)  # Asegura que el resultado tenga 2d dígitos
        medio = cuadrado[(len(cuadrado) // 2 - d // 2):(len(cuadrado) // 2 + d // 2)]
        x = int(medio)
        resultados.append(x)

        if x == 0:
            print("Advertencia: la secuencia cayó en 0. Final anticipado.")
            break

    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    semilla = ?
    n = ? # Cantidad de números a generar

    numeros = cuadrados_medios(semilla, n)

    for i, num in enumerate(numeros, 1):
        print(f"{i}: {num}")
