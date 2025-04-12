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
## Scatter Plot for Hidden Outliers

```R{r}
plot(df$Area, df$MajorAxisLength,pch = 20, main = "Scatter Plot for Outliers")
```
## Factor Variables Bar Plot

```R{r}
barplot(table(df$Class),cex.names=0.55)
```