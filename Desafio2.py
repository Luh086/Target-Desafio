#DESAFIO 2 - Sequência de Fibonacci

def sequencia_fibonacci(numero):
    a, b = 0, 1
    
    while b < numero:
        a, b = b, a + b
    
    if b == numero:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci:"))

if sequencia_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
