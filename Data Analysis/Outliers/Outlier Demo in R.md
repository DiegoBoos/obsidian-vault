## 📥 Load Dataset

```R{r}
df <- read.csv(file.choose(), sep = ",", header = TRUE)
head(df)
```
## 📦 Box Plots using 1.5*_IQR and adjusted IQR_

```R{r}
numeric_cols <- sapply(df, is.numeric)

# Default 1.5*IQR Boxplots
par(mfrow=c(2,2))

for (col in names(df)[numeric_cols]) {
  boxplot(df[[col]], horizontal = TRUE, pch = 20, main = col)
}

par(mfrow=c(1,1))

# Adjusted IQR range = 2
par(mfrow=c(1,2))

for (col in head(names(df)[numeric_cols], 2)) {
  boxplot(df[[col]], horizontal = TRUE, pch = 20, range = 2, main = paste(col, "(range=2)"))
}

par(mfrow=c(1,1))
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