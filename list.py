# List

print("#1")
lista1 = []
n = 20
for i in range(1, n+1):
    lista1.append(i*2)

print(lista1)

CANT = range(1, n+1)
lista2 = list(map(lambda x : x * 2, CANT))

print(lista2)

lista3 = [i*2 for i in range(1, n+1)]
print(lista3)
print("\n")

print("#2")
def triples(x):
    return x * 3

lista4 = list(map(lambda x : triples(x), CANT))

print(lista4)
print("\n")

print("#5")
lista5 = [4, 2, 4]

from itertools import permutations

comb = permutations(lista5, 3)

for i in comb:
    print(i)

print("\n")

print("#6")
tupla1 = (1, 2, 3, 4)
resultado = 0
for elm in tupla1:
    resultado += elm
print(resultado)
print("\n")

print("#11")
import sys

set1 = {473, "fsfb", (4, 3, 5)}
set2 = {4, 4, (3), "  wyduyvbfvubvuewhbvpwutbwtb2", 45643}
def compare_size(a, b):
    return sys.getsizeof(a), sys.getsizeof(b)

print(compare_size(set1, set2))


