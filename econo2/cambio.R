library(quantmod)
library(ggplot2)

getSymbols('CNYUSD=X',from='1950-01-01',to=Sys.Date())
data <- fortify(`CNYUSD=X`)
data$`CNYUSD=X.Close`<- 1/data$`CNYUSD=X.Close`
cambio <- data[,c(1,5)]
rm(data)
colnames(cambio) <- c('datas','cambio')
cambio <- cambio[complete.cases(cambio),]

for (i in 2:length(cambio$cambio)){
  cambio$var.cambio[1] <- NA
  cambio$var.cambio[i] <- cambio$cambio[i]/cambio$cambio[i-1] -1
}

cambio$positivo <- ifelse(cambio$var.cambio>=0,1,0)

ggplot(cambio,aes(x=datas,y=cambio,col=cambio)) + 
  geom_line() +
  theme_classic() + 
  scale_x_date(date_breaks = '2 year')

ggplot(cambio,aes(x=datas,y=cambio,col=as.factor(positivo))) + 
  geom_line() + 
  theme_classic()

ggplot(cambio,aes(x=datas,y=var.cambio,col=cambio)) +
  geom_line()+
  theme_classic()+
  scale_x_date(date_breaks = '2 year')

ggplot(cambio,aes(x=datas,y=var.cambio,col=cambio)) +
  geom_line()+
  theme_classic()+
  scale_x_date(date_breaks = '1 month',limits=as.Date(c('2018-01-01',Sys.Date())))

ggplot(cambio,aes(var.cambio)) + 
  geom_histogram(bins=100,alpha=1) + 
  geom_density(col='red') +
  #geom_vline(linetype='dashed',xintercept = 0,col='deeppink1',size=1) + 
  theme_classic()

lagzar <- function(p){
  df <- NULL
  yt <- NULL
  for(i in 1:(p+1)){
    yt <- cambio$var.cambio[(i):(nrow(cambio)-(p+1-i))]
    df <- cbind(yt,df)
  }
  for(i in 2:(p+1)){
    colnames(df)[i] <- paste0('L',i-1)
  }
  colnames(df)[1] <- 'yt'
  return(as.data.frame(df))
}

df <- lagzar(1)
m1 <- lm(data=df,yt~L1)
stargazer::stargazer(m1,type = 'text')

ggplot(data=df,aes(y=df[,1], x=L1)) + geom_point() +
  geom_smooth(method=lm,se=F,col='deeppink1') +
  theme_classic()

df <- lagzar(2)
m2 <- lm(data=df,yt~L1+L2)
stargazer::stargazer(m2,type = 'text')

df <- lagzar(3)
m3 <- lm(data=df,yt~L1+L2+L3)
stargazer::stargazer(m3,type = 'text')
