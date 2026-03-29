nome = input("Nome do eletrônico: ")
num1 = int(input("Quantos watts esse aparelho tem?: " ))
num2 = int(input("Tempo médio de uso diário em horas?: "))
operacao = (num1 * num2 * 30) / 1000
print("Consumo estimado:", operacao, "kWh/mês")