faturamento_diario = [22174.1664, 24537.6698, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

menor_faturamento = min(filter(lambda x: x > 0, faturamento_diario))

maior_faturamento = max(faturamento_diario)

dias_validos = [f for f in faturamento_diario if f > 0]
media_mensal = sum(dias_validos) / len(dias_validos)

dias_acima_media = sum(1 for f in faturamento_diario if f > media_mensal)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
