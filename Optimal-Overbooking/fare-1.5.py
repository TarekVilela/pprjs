global T, C, k, p 
T, C, k, p = 900, 170, 1.5, 0.9

fatorial = lambda x: x*fatorial(x-1) if x > 0 else 1
binomial = lambda x,y: fatorial(x)/(fatorial(y)*fatorial(x-y))
F = lambda i: 0 if i <= C else (k+1)*T*(i - C)
prob = lambda B,i: binomial(B,i)*(p**i)*((1-p)**(B-i))

def R(B):
    receitaEsperada = 0
    for i in range(1,B+1):
        receitaEsperada += prob(B,i)*(B*T-F(i))
    return receitaEsperada