library(mFilter)
library(ggplot2)
desemprego$ordem <- seq(1,nrow(desemprego),1)

ggplot(data=desemprego,aes(x=ordem,y=X2)) +
  geom_line()

teste.hp <- hpfilter(desemprego$X2,type=c('lambda'),freq=1600)
plot(teste.hp)

class(teste.hp$trend[1])

