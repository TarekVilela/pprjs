import math

def binomial(x,y):
    r = math.factorial(x)/(math.factorial(y)*math.factorial(x-y))

    return r

def F(i,C,k=2.2,T=359.14):
    if i <= C:
        f = 0
    elif i > C:
        f = (k+1)*T*(i - C)

    return f

def prob(p,B,i):
    prob = binomial(B,i)*(p**i)*((1-p)**(B-i))
    
    return prob

def R(B,C=151,p=0.8,T=359.14):
    receitaEsperada = 0
    for i in range(1,B+1):
        receitaEsperada += prob(p,B,i)*(B*T-F(i,C))
    
    return receitaEsperada
