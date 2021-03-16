library(gpl)
library(readr)
coin <- read_csv("Desktop/python scraping/file.csv",na = "-")
View(coin)
coin <- na.omit(coin)
plot(x = coin$date , y = coin$mean, type = 'l', col='green')
lines(x= coin$date, y = coin$high ,type = 'l', col='red')
lines(x= coin$date, y = coin$low ,type = 'l', col='orange')

hist(coin$low)

coin[order(coin$date ),]


coin$date <- as.Date(coin$date)
is.numeric.Date(coin$date)
typeof(coin$high)
head(coin$date)
coin$mean <- rowMeans(coin[,c('high', 'low')], na.rm=TRUE)
coin$mean


X<- data.frame(Placebo=c(5,8,7,7,10,8),
               T2=c(4,6,6,3,5,6),
               T3=c(6,4,4,5,4,3),
               T4=c(7,4,6,6,3,5),
               T5=c(9,3,5,7,7,6))
delai <- stack(X)$values
traitement <- stack(X)$ind
traitement
tapply(delai, traitement, summary)
plot(delai~traitement)
mon.aov <- aov(delai~traitement)
summary(mon.aov)
lm(formula=delai ~ traitement)
par(mfrow=c(2,2))
plot(lm(mon.aov),col.smouth="red")
bartlett.test(delai~traitement)
bartlett.test(BWT ~ as.factor(SMOKE))
levene.test(delai~traitement)
