#Aula 07 - Automatizando lista de compras

lista = [] #isto é uma lista em python

print("Digite os itens da sua lista de compras: ")
print("Quando terminar digite 'sair': ")

while True:
  item = input("item: ")
  if item == "sair":
    break
  else:
    lista.append(item) #função da estrutura lista (anexar na lista)
print("Sua lista de compras: \n")

for produto in lista:
  print(" - ",produto)
