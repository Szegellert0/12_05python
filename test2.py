import random
lista = []
def veletlen():
    hossz = 20
    lista = []
    for item in range(hossz):
        lista.append(random.randint(1,50))
    return lista

def kiirVeletlen():
    for i in range(20):
        print(veletlen()[i])

def kiir():
    for item in veletlen():
        print(item, end=" ")

def osszeAd():
    sum = 0
    for item in veletlen():
        sum = sum + item
    return sum 

def legnagyobbElem():
    max = list[0]
    for item in veletlen():
        if item > max:
            max = item
    return max
    
veletlen()
kiir()
print()
print(f"A lista eleinek az összege: {osszeAd()}")
print(f"A lista eleinek legnagyobb értéke: {legnagyobbElem()}")
#kiirVeletlen()