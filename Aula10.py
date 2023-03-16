#Criando uma lista de números 
numeros = [10, 20, 30, 40, 50]

#Iniciando a variável que irá armazenar o maior número
maior_numero = numeros[0]

#Usando um loop for para percorrer a lista e econcontrar o maior número
for numero in numeros: 
    if numero > maior_numero:
        maior_numero = numero

#Imprimindo o resulto
print("O maior número na lista é: ", maior_numero)