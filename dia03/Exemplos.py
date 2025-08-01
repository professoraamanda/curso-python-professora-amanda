# Aula 03 - Calculadora de gastos

# Entrada de dados
salario = float(input("Digite seu salário: "))
aluguel = float(input("Quanto gasta com aluguel: "))
mercado = float(input("Quanto gasta no mercado: "))
outros = float(input("Outros gastos fixos: "))

# Processamento
total_gasto = aluguel + mercado + outros
saldo = salario - total_gasto

# Saída
print("Você ainda tem R$", saldo)


# --- Lembrete para beber água ---
import time

print("Lembrete: beba água agora!")
time.sleep(3600)  # pausa de 1 hora
print("Ei, hora de beber água de novo!")
