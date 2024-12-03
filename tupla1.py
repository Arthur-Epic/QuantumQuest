# Definindo a tupla
minha_tupla = (10, 20, 30, 40, 50)


minha_lista = list(minha_tupla)


print(minha_lista)
print("-"*30)
print(type(minha_tupla))
print("-"*30)
print(type(minha_lista))
print("-"*30)


minha_lista.append(60)
minha_lista.append(70)


print(minha_lista)


minha_lista.pop(0)


print(minha_lista)


minha_lista.pop()


print(minha_lista) 
print("-"*30)


print("Primeiro elemento da lista:", minha_lista[0])
print("-"*30)


print("Quantidade de elementos na lista:", len(minha_lista))
print("-"*30)


pessoa = {
    "Nome": "Arthur",
    "Idade": 22,
    "Profissão": "Beto"
}


print(pessoa["Nome"])


for valor in pessoa.values():
    print(valor)