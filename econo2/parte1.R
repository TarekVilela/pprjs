library(ggplot2)

# pib a preços de 1995
pib$ordem <- seq(1,nrow(pib),1)
pib <- pib[1:89,]
pib$X2 <- pib$X2/100000
pib$ano <- substr(pib$X1,1,4)

ggplot(pib,aes(x=ordem,y=X2)) +
  geom_line()+
  geom_smooth(method=lm,se=F) +
  theme_classic()

ggplot(pib,aes(x=ordem,y=X2,col=ano)) +
  geom_line()+
  geom_smooth(method=lm,se=F)+
  theme_classic()

m1 <- lm(data=pib,X2~ordem)
summary(m1)

acf(m1$residuals)
hist(m1$residuals)
plot(y=m1$residuals,x=predict(m1))

(pib$X2[nrow(pib)]/pib$X2[1]-1)
