arqs_filmes = []
arqs_jogos = []
for i in range(1,41):
    arqs_filmes.append('dados-'+str(i)+'-filmes.csv')
    arqs_jogos.append('dados-'+str(i)+'-jogos.csv')

with open('.csv', 'w') as saida:
    for j in arqs_filmes:
        with open(j) as entrada:
            for linha in entrada:
                saida.write(linha)

with open('.csv', 'w') as saida:
    for j in arqs_jogos:
        with open(j) as entrada:
            for linha in entrada:
                saida.write(linha)