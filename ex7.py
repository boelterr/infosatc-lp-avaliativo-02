#Gabriel Boelter 2190
#A
listaf = ['Donnie Darko', 'Velozes e Furiosos 1'] 
listaf.append('Kingsman')
listaf.append('LaLaLand')

listaj = ['God of War', 'The Witcher']

listaj.append('Valorant')
listaj.append('Forza')

listal = ['Senhor dos Aneis', 'O Hobbit']

listal.append('Harry Potter')
listal.append('Percy Jackson')

listae = ['Corrida, Futebol']

listae.append('F1')
listae.append('Basquete')

#B
lista_nova = listaf + listaj + listal + listae
#C
print(listal[1])
#D
del listae[1]
#E
lista_nova.append("Disciplina de Cálculo") 
lista_nova.append("Disciplina de Ciência") 

print("Lista de filmes",listaf)
print("Lista de jogos",listaj)
print("Lista de livros",listal)
print("Lista de esportes",listae)
print("Todas as listas", lista_nova)