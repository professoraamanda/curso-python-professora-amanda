# Calculadora de frete

# Entrada de dados
distancia = float(input("Qual é a distância (em km)?\n"))
tipo_de_entrega = input("Qual é o tipo de entrega?\n")

# Processamento com if/elif/else
if tipo_de_entrega == "normal":
    valor_do_frete = distancia * 0.5
elif tipo_de_entrega == "expressa":
    valor_do_frete = distancia * 0.8
else:
    print("Tipo de entrega inválido!")
    valor_do_frete = None

# Saída formatada
if valor_do_frete is not None:
    print("O valor do frete é R$", round(valor_do_frete, 2))
