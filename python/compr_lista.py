'''
numeros = [1,2,3,4,5]

numeros_dobrados = list()

for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)
'''

numeros = [1,2,3,4,5]
def dobro(numero):
    return numero * 2
numeros_dobrados = [dobro(numero) for numero in numeros]
print(numeros_dobrados)