#Gabriel Boelter 2190
print("Lista de compras para o computador")

lista = []

lista.append("Gabinete Cooler Master")
lista.append("16GB de Memória RAM")
lista.append("Processador Intel i9 9900KF")
lista.append("Placa-mãe AORUS")
lista.append("Fonte 600W")
lista.append("NVIDIA GeForce RTX 2080 TI")
lista.append("Water Cooler Sangue Frio")

del lista[0]
del lista[5]

print("Seu carrinho para a compra" ,lista)