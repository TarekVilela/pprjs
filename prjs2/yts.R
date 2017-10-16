setwd("/home/tarek/Documentos/R - Projetos/yts")
library(readr)
library(ggplot2)

ggplot() + 
  geom_bar(data=yts2,aes(X2,fill=as.character(X2))) + h + 
  labs(x='Ano de lançamento',y='Contagem') + 
  ggtitle('YIFY: ano de lançamento de filmes compartilhados')

ggsave('yts-frequencia.png',type = 'cairo-png',scale=2,dpi = 500)