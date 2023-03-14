import random as rd
Q=int(input("choissisez taille tableau"))
V=[]
for k in range(Q):
    V+=[rd.randint(0,1)]

print(V)
def calcul_indice (T):
    p=0
    i=0
    for k in range (len(T)):
        if k%2==0:
            p+=T[k]
        else:
            i+=T[k]
    return p,i
print(calcul_indice(V))