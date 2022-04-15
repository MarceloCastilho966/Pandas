nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
print (nomes_carros)
print ("1------------------------------\n")

for item in nomes_carros:
    print(item)
print ("2------------------------------\n")
    
carro_1, carro_2, carro_3, carro_4 = nomes_carros

print (carro_1)
print (carro_2)
print (carro_3)
print (carro_4)

print ("3------------------------------\n")


## Com o _ eu consigo ignorar algumas tuplas
## Com o *_ eu consigo ignorar todos a frente

_, A, _, B = nomes_carros

print (A, B)
print ("4------------------------------\n")

_, C, *_ = nomes_carros

print (C)
print ("5------------------------------\n")


# Lista de Valores
valores = [88078.64, 106161.94, 72832.94, 124549.07]
print (valores)
print ("6------------------------------\n")

# Fazendo uma interação entre a lista e as Tuplas
print (list(zip(nomes_carros, valores)))
print ("7------------------------------\n")

for item in zip(nomes_carros, valores):
    print (item)
print ("8------------------------------\n")

for carro, valor in zip(nomes_carros, valores):
    print (carro,"= R$", valor)
print ("9------------------------------\n")

# utilizando o IF para filtragem
for carro, valor in zip(nomes_carros, valores):
    if (valor > 100000):
        print (carro,"= R$", valor)


