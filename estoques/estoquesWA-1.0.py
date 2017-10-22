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

if q > sum(estoque):
    print('Não há estoque suficiente para realizar a venda!')

else:
    custo_final = (custo_total/sum(estoque))*q
    print('Cost of goods sold: ',custo_final)
