---
title: "Inference Demonstration"
author: "David Marsh"
date: "01/01/2024"
output: pdf_document
---
## 🔧 Setup

```R{r}
knitr::opts_chunk$set(fig.width=5, fig.height=5,
                      fig.path='Figs/', echo = TRUE)

# This sets the working directory
knitr::opts_knit$set(root.dir = 'Users/diegobolanos/Documents/GeneralPracticeDatasets')
```

```R{r}
# Optional: clear environment
# if(!is.null(dev.list())) dev.off()
# cat("\014") 
# rm(list=ls())
options(scipen=9)
```
## 📦 Load Packages

```R{r}
if(!require(HSAUR)){install.packages("HSAUR")}
library("HSAUR")

if(!require(pastecs)){install.packages("pastecs")}
library("pastecs")
```
## 📥 Load and Summarize Data

```R{r}
data(water)
Water <- water
head(Water)
stat.desc(Water)
```
## 🧪 One-Sample t-test

```R{r}
t.test(Water$mortality, mu=1200)
```
## 🌊 Density Plots

```R{r}
plot(density(Water$mortality), main="Mortality")
rug(Water$mortality, col=2)

plot(density(Water$hardness), main="Hardness")
rug(Water$hardness, col=2)
```
## 📏 Normality Check (Shapiro and Q-Q Plots)

```R{r}
shapiro.test(Water$hardness)
shapiro.test(Water$mortality)

qqnorm(Water$hardness, main="Is Hardness Normal?", pch=20)
qqline(Water$hardness)

qqnorm(Water$mortality, main="Is Mortality Normal?", pch=20)
qqline(Water$mortality)
```
### 🔁 Loop for Normality Testing

```R{r}
for (i in 1:ncol(df)) {
  if (is.numeric(df[,i])) {
      print(names(df[i]))
      print(shapiro.test(df[[i]]))
  }
}

for (i in 1:ncol(df)) {
  if (is.numeric(df[,i])) {
      qqnorm(df[[i]], main=(names(df[i])), pch=20)
      qqline(df[[i]])
  }
}
```
## 📊 Boxplots by Group

```R{r}
boxplot(hardness ~ location, data=Water, main="Hardness by Location")

boxplot(mortality ~ location, data=Water, main="Mortality by Location")
```
## 📉 Variance and Mean Comparison Between Groups

```R{r}
var.test(mortality ~ location, data = Water)
t.test(mortality ~ location, data = Water, var.equal = TRUE)
wilcox.test(hardness ~ location, data = Water, exact = FALSE)
```
### 🔁 Loop for Variance Checks

```R{r}
group_col <- "location"

for (col in names(Water)[numeric_cols]) {
  print(paste("Variance test for:", col))
  print(var.test(as.formula(paste(col, "~", group_col)), data = Water))
}
```
## 🔄 Correlation

```R{r}
plot(hardness ~ mortality,
     data = Water,
     pch = 20, col = 6,
     main = "Hardness vs. Mortality")
cor(Water$hardness, Water$mortality, method = "spearman")
```
## 🔢 Chi-square Test  

```R{r}
t = table(df$Class_DABO, df$GATA_DABO)
chisq.test(t)
round(chisq.test(t)$expected, 0)
```