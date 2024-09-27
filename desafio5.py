def inverter_string(string):
    invertida = ''

    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]

    return invertida


original = input("Digite uma frase para ser invertida: ")

invertida = inverter_string(original)

print("Frase original:", original)
print("Frase invertida:", invertida)
