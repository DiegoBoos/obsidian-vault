---
title: "ANOVA Demonstration"
author: "David Marsh"
date: "01/01/2024"
output: pdf_document
---
```R{r setup, include=FALSE}
knitr::opts_chunk$set(fig.width=5, fig.height=5,
                      fig.path='Figs/', echo = TRUE)
#This sets the working directory
knitr::opts_knit$set(root.dir = '/Users/diegobolanos/Documents/GeneralPracticeDatasets')
```

```R{r}
#if(!is.null(dev.list())) dev.off()
#cat("\014") 
#rm(list=ls())
options(scipen=9)
```
This section loads and attaches all the necessary packages.

```R{r}
#Load packages
if(!require(pastecs)){install.packages("pastecs")}
library("pastecs")

if(!require(tinytex)){install.packages("tinytex")}
library("tinytex")

```
### Read in Data

```R{r}
df <- read.table("PROG8435-ANOVA-Demo.txt", sep=",", header=TRUE)
df <-as.data.frame(df)
head(df,2)
table(df$Page)
df$Page <- as.factor(df$Page)
df$User <- as.factor(df$User)
```

```R{r}
#Comparing Pages
boxplot(Time ~ Page, data=df,main="Time spent on each page (secs)")

#Comparing Users
boxplot(Time ~ User, data=df,main="Time spent on each page (secs)")
```
 
```R{r}
#One-Way ANOVA
summary(aov(Time ~ Page, data=df))
print(" ")
summary(aov(Time ~ User, data=df))
print(" ")
ANOVA_page <- aov(Time~Page, data=df)
summary(ANOVA_page)
```

```R{r}
#Two-Way ANOVA
anova_two_page <- aov(Time~Page + User, data = df)
summary(anova_two_page)
```

```R{r}
Hours <- read.csv("ANOVA-Demo-2.txt", sep=",", header=TRUE)
Hours <-as.data.frame(Hours)
head(Hours)

anova_two_way <- aov(Hr ~ Camp + Program, data = Hours)
summary(anova_two_way)

# Testing normality
plot(density(Hours$Hr,pch=20))
rug(Hours$Hr)

qqnorm(Hours$Hr)
qqline(Hours$Hr)

shapiro.test(Hours$Hr)
var.test(Hours$Hr ~ Camp, data=Hours)

boxplot(Hr ~ Camp + Program, data = Hours,
        main="Hours Spent by Campus and Program")
```

More Chi-Sq Practice

```R{r}
t <- table(Hours$Camp,Hours$Program)
t

chisq.test(t)
round(chisq.test(t)$expected,0)
```

For Practice!
The dataset contains the Mark at the midway point of a class, and indicators
for Attendance, Coming to Office Hourse, Using Discussion Forums and 
Final Status in the Course

See if you can compare marks on a variety of metrics or create two-way ANOVAs

```R{r}
Marks <- read.csv("SampleMarks.txt", sep=",", header=TRUE)
Marks <-as.data.frame(Marks)

head(Marks)

```


