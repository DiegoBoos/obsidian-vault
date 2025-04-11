---
title: "PROG8435-Demo-Summarize"
author: "David"
date: "01/01/2024"
output: pdf_document
---
Basic set up

```R{r}
# if(!is.null(dev.list())) dev.off()
# cat("\014")
# rm(list=ls())
options(scipen=9)
```

Loading packages

```R{r}
if(!require(pastecs)){install.packages("pastecs")}
library("pastecs")
```

Loading the Dataset

```R{r}
df <- read.csv("df.csv", header=TRUE, sep=",")
df <- as.data.frame(df)
head(df, 5)
```

Rename all the Variables

```R{r}
colnames(df_DABO) <- paste(colnames(df), "DABO", sep = "_")
head(df_DABO,10)
```

Transforming categorical variables to a factor variables

```R{r}
df_DABO$plant_DABO <- as.factor(df_DABO$plant_DABO)
```

Data summary

```R{r}
df_summary_DABO <- stat.desc(df_DABO)
format(df_summary_DABO,digits=2)
```