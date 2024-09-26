#DESAFIO 3 - Descubra a lógica

# letra a)
sequencia_a = [1, 3, 5, 7]
elemento_a = sequencia_a[-1] + 2
print("Na letra A, o próximo elemento da sequência é:", elemento_a )

# letra b)
sequencia_b = [2, 4, 8, 16, 32, 64]
elemento_b  = sequencia_b[-1] * 2
print("Na letra B, o próximo elemento da sequência é:", elemento_b)

# letra c)
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
elemento_c  = sequencia_c[-1] + len(sequencia_c)**2
print("Na letra C, o próximo elemento da sequência é:", elemento_c )

# letra d)
sequencia_d = [4, 16, 36, 64]
elemento_d = (len(sequencia_d) + 1)**2
print("Na letra D, o próximo elemento da sequência é:", elemento_d)

# letra e)
sequencia_e = [1, 1, 2, 3, 5, 8]
elemento_e = sequencia_e[-1] + sequencia_e[-2]
print("Na letra E, o próximo elemento da sequência é:", elemento_e)

# letra f)
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
elemento_f  = sequencia_f[-1] + 181
print("Na letra F, o próximo elemento da sequência é:", elemento_f)
