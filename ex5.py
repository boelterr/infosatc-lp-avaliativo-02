#Gabriel Boelter 2190
nome = input("Verifique se seu nome esta na lista: ")

lista = []
lista.append("Gabriel")
lista.append("Thiago")
lista.append("Augusto")
lista.append("Elias")
lista.append("Dj Bratti SC")

if (nome) in lista:
    print("Sim, está na lista!")
else:
    print("Não está na lista")

print("Os nomes na lista são",(lista))