
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
```
## 🌊 Density Plots

```R{r}
par(mfrow=c(1,2))

for (col in c(head(names(df)[numeric_cols], 2))) {
  plot(density(df[[col]]), main = paste("Density of", col))
  rug(df[[col]], col = 2)
}

par(mfrow=c(1,1))
```
## 🔎 Scatter Plot for Hidden Outliers

```R{r}
plot(df[[names(df)[numeric_cols][1]]], df[[names(df)[numeric_cols][2]]],
     pch = 20, main = "Scatter Plot for Outliers")
```
## 🧩 Factor Variables Bar Plot

```R{r}
factor_cols <- sapply(df, is.factor)

for (col in names(df)[factor_cols]) {
  barplot(table(df[[col]]), cex.names = 0.75, main = col)
}

```