ipca$ordem <- seq(1,nrow(ipca),1)
x <- rep(1:4,each=3,nrow(ipca)/12)[1:nrow(ipca)]

ipca$trimestre <- x

ipca$d1 <- ifelse(ipca$trimestre==1,1,0)
ipca$d2 <- ifelse(ipca$trimestre==2,1,0)
ipca$d3 <- ifelse(ipca$trimestre==3,1,0)
ipca$d4 <- ifelse(ipca$trimestre==4,1,0)

m2 <- lm(data=ipca,X1~d2+d3+d4)
summary(m2)

ggplot(data=ipca,aes(x=ordem,y=X1)) +
  geom_line() +
  geom_smooth(method=lm,se=F)

plot(y=m2$residuals,x=predict(m2))
acf(m2$residuals)

