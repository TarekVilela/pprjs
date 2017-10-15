library(readr)
library(ggplot2)
library(ggridges)

friends <- read_csv("friends.csv", col_names = FALSE)
colnames(friends) <- c('nome','nrevws','nota','temporada','neptemp')

ordem <- c('S1','S2','S3','S4','S5','S6','S7','S8','S9','S10')
h <- theme(legend.position="none")

ggplot(data = friends,aes(x=temporada,y=neptemp,fill=nota)) + 
  geom_tile() + 
  labs(x = 'Temporada',y='Episódio') +
  scale_x_discrete(limits=ordem) + 
  scale_fill_gradient(low='black',high='gold')
  
ggplot(data=friends,aes(x=nota,y=temporada,fill=temporada)) + 
  geom_density_ridges(alpha=0.65) + 
  labs(x = 'Nota',y='Temporadas') +
  scale_y_discrete(limits=ordem) + 
  geom_vline(xintercept = mean(friends$nota),linetype = 'dotted',alpha=0.4) + 
  h 

ggplot(data = friends,aes(x=temporada,y=nota,color=temporada,fill=temporada)) + 
  geom_violin(alpha=0.6) + 
  geom_jitter() + 
  labs(x = 'Temporada',y='Nota') + 
  scale_x_discrete(limits=ordem) + 
  h 

ggplot(data = friends,aes(x=as.character(neptemp),y=nota,color=as.character(neptemp),fill=as.character(neptemp))) + 
  geom_violin(alpha=0.6) + 
  geom_jitter() + 
  labs(x = 'Episódio na temporada',y='Nota') +
  scale_x_discrete(limits=1:25) + 
  h
