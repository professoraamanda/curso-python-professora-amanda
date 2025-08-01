import time

# Entrada do tempo
tempo = int(input("Quantos segundos você quer contar?\n"))

# Contagem regressiva
for i in range(tempo, 0, -1):
    print(i)
    time.sleep(1)

print("Tempo esgotado!")
