# Leitura do peso de peixes
peso = float(input("Digite o peso dos peixes em quilos: "))

# Verifica se há excesso de peso
excesso = peso - 50  # Calcula a quantidade de quilos além do limite

if excesso <= 0:
    excesso = 0
    multa = 0
else:
    multa = excesso * 4  # Calcula o valor da multa (R$ 4,00 por quilo excedente)

# Exibe o resultado
print("Excesso de peso: %.2f kg" % excesso)
print("Valor da multa: R$ %.2f" % multa)
