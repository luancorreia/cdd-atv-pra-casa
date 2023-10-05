mt= int(input('Digite um valor aleatório:'))
base=[0] * mt
a=[0] * mt
b=[0] * mt
cont=0
for x in range(mt):
    a[x] = int(input('Digite um valor pra A:'))
    b[x] = int(input('Digite um valor pra B:'))
    base[x] = a[x] + b[x]
for x in a:
    cont +=1
print(a)
print(b)
print(base)
print(cont)