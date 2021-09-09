#Gabriel Boelter 2190
nome = input("Digite um nome para verificar a posição que está na lista: ")

lista = []
lista.append("Gabriel")
lista.append("Thiago")
lista.append("Augusto")
lista.append("Elias")
lista.append("Dj Bratti SC")

print("O nome {} está na posição: ".format(nome), lista.index(nome))

