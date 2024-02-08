def fibonacci(n):
    fibo_sequence = [0, 1]
    while fibo_sequence[-1] < n:
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
    return fibo_sequence

def verifica_pertence(numero):
    fibo_sequence = fibonacci(numero)
    if numero in fibo_sequence:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
verifica_pertence(numero)