import math
import csv

print('--- Defina os parâmetros ---\n')
global T
global C
global k
global p
T = float(input('T: '))
C = float(input('C: '))
k = float(input('k: '))
p = float(input('p: '))

def binomial(x,y):
    r = math.factorial(x)/(math.factorial(y)*math.factorial(x-y))

    return r

def F(i):
    if i <= C:
        f = 0
    elif i > C:
        f = (k+1)*T*(i - C)

    return f

def prob(B,i):
    prob = binomial(B,i)*(p**i)*((1-p)**(B-i))
    
    return prob

def R(B):
    receitaEsperada = 0
    for i in range(1,B+1):
        receitaEsperada += prob(B,i)*(B*T-F(i))
    
    return receitaEsperada