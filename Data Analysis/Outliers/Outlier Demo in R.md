```R{r}
# Summaries of the data with density plots

par(mfrow=c(2,2))   

for (i in 1:ncol(df)) {
  if (is.numeric(df[,i])) {
    plot(density(df[,i]), main=names(df)[i])
    rug(df[,i],col=2)
  }
  }

par(mfrow=c(1,1))

```

```R{r}
# Find Outliers

par(mfrow=c(2,2))

for (i in 1:ncol(df)) {
  if (is.numeric(df[,i])) {
      boxplot(df[,i], 
              main=names(df)[i],
              ylab=names(df)[i],
              horizontal = TRUE)
  }
}

par(mfrow=c(1,1))

```

## Code to Deal with outliers
### delete the row

```{r}
plot(density(df$x6), pch=6)
rug(df$x6,col=2)
nr <- which(df$x6 == 0)  #Find row number with x6 = 0
df <- df[-c(nr),]
plot(density(df$x6), pch=6)
rug(df$x6,col=2)

plot(density(df$x2), pch=6)
rug(df$x2,col=2)
head(df[rev(order(df$x2)),],3)   #See the top three for fun
nr <- which(df$x2 == max(df$x2))  #Row number for max value 
df <- df[-c(nr),]
plot(density(df$x2), pch=6)
rug(df$x2,col=2)

```

#### Adjust the value
Should only be done is very rare and specific circumstances

```R{r}
plot(density(df$x3), pch=6)
rug(df$x3,col=2)
df$x3 <- ifelse(df$x3 == min(df$x3),mean(df$x3),df$x3)  #Replaces min value with the mean
plot(density(df$x3), pch=6)
rug(df$x3,col=2)

```
## Scatter Plot for Hidden Outliers

```R{r}
plot(df$Area, df$ConvexArea, 
     pch = 20, 
     main = "Scatter Plot for Hidden Outliers in Area",
     xlab = "Area",
     ylab = "Convex Area")
```
## Factor Variables Bar Plot

```R{r}
barplot(table(df$Class),cex.names=0.55)
```