def calcular_pi(n):
    pi = 0
    signo = 1         # Comienza positivo
    denominador = 1   # El primer denominador es 1

    # El ciclo se repite 'n' veces (el número de iteraciones)
    for i in range(n):
        # 1. Calculamos la fracción actual con su signo y la sumamos al acumulador 'pi'
        termino = signo * (1 / denominador)
        pi = pi + termino
        
        # 2. Preparamos el denominador para la siguiente iteración (1, 3, 5, 7...)
        denominador = denominador + 2
        
        # 3. Alternamos el signo multiplicando por -1
        signo = signo * -1

    # Al terminar el ciclo, multiplicamos todo por 4 según la fórmula
    return pi * 4

# --- Ejemplo de uso ---
# Entre más grande sea 'n', más precisa será la aproximación
terminos = 100000
valor_aprox = calcular_pi(terminos)
print(f"Aproximación con {terminos} términos: {valor_aprox}")
