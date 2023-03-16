minha_lista = [] #Criando uma lista vazia 

for i in range(5): 
    minha_lista.append(i + 1) #não irá iniciar com o zero 
    
print(minha_lista)

print('-----------------------------------------------')

minha_lista2 = [10, 1, 8, 3, 5]
total = 0

for i in range(len(minha_lista2)):
    total += minha_lista2[i]

print(total)

print('-----------------------------------------------')

minha_lista3 = [10, 1, 8, 3, 5]
total1 = 0

for i in minha_lista3:
    total1 += i

print(total1)