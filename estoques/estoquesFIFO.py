estoque = []
custo = []

while True:
    estoque_add = input('Quantidade adquirida: ')
    if estoque_add == '':
        break
    else:
        estoque.append(int(estoque_add))
        custo_add = input('Custo de aquisição: ')
        custo.append(float(custo_add))
        
print('\n')
print('Estoque = ' + str(sum(estoque)))

custo_total = 0

for i in range(len(custo)):
    custo_total += custo[i]*estoque[i]

print('Custo total =',custo_total)

q = int(input('Quantidade vendida: '))

custo_total = 0

if q > sum(estoque):
    print('Não há estoque suficiente para realizar a venda!')

else:
    usados = []
    vezes = 0
    for i in range(0,len(estoque)):
        if q > estoque[i]:
            usados.append(estoque[i])
            q = q - estoque[i]
            vezes += 1 

        elif q <= estoque[i]:
            usados.append(q)
            q = 0
            vezes += 1
            break
        
    custo = custo[0:len(usados)]  
    for i in range(0,len(usados)):
        custo_total += usados[i]*custo[i]

    print('Cost of goods sold:',custo_total)