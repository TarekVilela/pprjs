import math

print('--- Defina os parâmetros ---\n')
global T, C, k, p 
T, C, k, p = float(input('T: ')), float(input('C: ')), float(input('k: ')), float(input('p: '))
print('\n')

binomial = lambda x,y: math.factorial(x)/(math.factorial(y)*math.factorial(x-y))
F = lambda i: 0 if i <= C else (k+1)*T*(i - C)
prob = lambda B,i: binomial(B,i)*(p**i)*((1-p)**(B-i))

def R(B):
    receitaEsperada = 0
    for i in range(1,B+1):
        receitaEsperada += prob(B,i)*(B*T-F(i))
    
    return receitaEsperada