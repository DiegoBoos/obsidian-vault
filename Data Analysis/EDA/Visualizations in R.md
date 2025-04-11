```R{r}
##################################################
### Bar Plots                                  ##
##################################################

par(mfrow=c(2,2))
for (i in 1:ncol(df)) {
  if (is.factor(df[[i]])) {
    ct <- table(df[[i]])
    barplot(ct, main=names(df)[i])
  }
}
par(mfrow=c(1,1))

##################################################
### Histograms                                 ##
##################################################

par(mfrow=c(2,2))
for (i in 1:ncol(df)) {
  if (is.factor(df[[i]])) {
    ct <- table(df[[i]])
    hist(ct, main=names(df)[i])
  }
}
par(mfrow=c(1,1))

##################################################
### Box Plots                                  ##
##################################################

par(mfrow=c(2,2))
for (i in 1:ncol(df)) {
  if (is.factor(df[[i]])) {
    ct <- table(df[[i]])
    boxplot(ct, main=names(df)[i])
  }
}
par(mfrow=c(1,1))

boxplot(df$McCain_BDSA, main="Distribution of McCain Support",
        xlab="Percent of McCain Support", col=5, horizontal=TRUE, pch=20)

boxplot(McCain_BDSA ~ Region_BDSA, data=df,
        main="McCain Support by Region",
        xlab="Region", col=4, pch=20)

##################################################
### Density Plots                              ##
##################################################

par(mfrow=c(2,2))
for (i in 1:ncol(df)) {
  if (is.numeric(df[[i]])) {
    plot(density(df[[i]]), main=names(df)[i])
    rug(df[[i]], col=2)
  }
}
par(mfrow=c(1,1))

##################################################
### Scatter Plot                               ##
##################################################

plot(Unemployment_BDSA ~ Income_BDSA, data=df,
     col=6, pch=4, main="Income vs Unemployment",
     xlab="Income", ylab="Unemployment Rate")
abline(coef = c(6,0))  # intercept = 6, slope = 0
```