#DESAFIO 2 - Sequência de Fibonacci

def is_fibonacci_number(num):

    fib_sequence = [0, 1]
    while fib_sequence[-1] < num:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

user_number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

result = is_fibonacci_number(user_number)
print(result)
