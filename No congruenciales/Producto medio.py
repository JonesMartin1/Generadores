def producto_medio(x0, x1, n):
    """
    Método del Producto Medio de Von Neumann:
    Fórmula:
        X_{n+1} = extraer_digitos_centrales(X_n * X_{n-1})

    Recomendaciones:
    - x0 y x1 deben tener la misma cantidad de dígitos, preferentemente 4 o 6.
    - El resultado debe tener al menos el doble de dígitos para extraer los del centro.
    - Se normaliza dividiendo por 10^d para obtener un número en [0, 1).

    Parámetros:
    - x0: primera semilla (entero con longitud par)
    - x1: segunda semilla (igual longitud que x0)
    - n: cantidad de números a generar

    Retorna:
    - Lista de números pseudoaleatorios
    """
    resultados = []
    d = len(str(x0))

    if d != len(str(x1)) or d % 2 != 0:
        raise ValueError("Las semillas deben tener la misma cantidad par de dígitos.")

    prev, curr = x0, x1

    for _ in range(n):
        prod = str(prev * curr).zfill(2 * d)  # Asegura 2d dígitos
        medio = prod[(len(prod) // 2 - d // 2):(len(prod) // 2 + d // 2)]
        next_val = int(medio)
        resultados.append(next_val)
        if next_val == 0:
            print("Advertencia: la secuencia cayó en 0. Final anticipado.")
            break

        # Actualizar para la próxima iteración
        prev, curr = curr, next_val

    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    x0 = ?
    x1 = ?
    n = ? # Cantidad de números a generar

    numeros = producto_medio(x0, x1, n)

    for i, num in enumerate(numeros, 1):
        print(f"{i}: {num}")
