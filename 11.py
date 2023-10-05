
import random
v=[0] *30
cont = 0
for x in range(30):
    v[x] = random.randint(1,50)
n = int(input('Digite um numero até 50:'))
for y in range(30):
    if n == v[y]:
        cont +=1
print(f'Seu numero se repete na lista: {cont} vezes')
print(v)
