def fibonacci(n):

    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    if n in fib:
        return fib, f"O número {n} pertence à sequência de Fibonacci."
    else:
        return fib, f"O número {n} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = int(input("Digite um número: "))
resultado, mensagem = fibonacci(numero)
print(resultado)
print(mensagem)