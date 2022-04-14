nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])

print(nomes_carros[0])

print(nomes_carros[1])

print(nomes_carros[-1])

## -------------------------------------


print(nomes_carros[1:3])

# Tuplas dentro de Tuplas
nomes_carros2 = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5',
                       ('Fusca', 'Gol', 'C4')])

print (nomes_carros2 [-1][1])