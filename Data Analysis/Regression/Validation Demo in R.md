---
title: "Validation"
author: "David"
date: "10/10/2024"
output: pdf_document
---
```R{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```
### The code chunk below gives the summary of Seatbelts

```R{r}
data(Seatbelts)
SB <- na.omit(as.data.frame(Seatbelts))
head(SB,5)
```
### Break in to Train and Test Groups

```R{r, echo=FALSE}
# Choose sampling rate
sr <- 0.8

# Find the number of rows of data
n.row <- nrow(SB)

#Choose the rows for the training sample 

set.seed(8891)
training.rows <- sample(1:n.row, sr*n.row, replace=FALSE)

#Assign to the training sample

train <- subset(SB[training.rows,])

# Assign the balance to the Test Sample

test <- subset(SB[-c(training.rows),])

#summary(SB)
#summary(test)
#summary(train)

#Compare some summaries

#round(mean(SB$PetrolPrice),4)
round(mean(train$PetrolPrice),6)
round(mean(test$PetrolPrice),6)

wilcox.test(train$PetrolPrice, test$PetrolPrice)
```
### Split in to Test/Train/Validation

```R{r}
# Choose sampling rate
tr <- 0.6
ts <- 0.2
vd <- 0.2

# Find the number of rows of data
n.row <- nrow(SB)

#Choose the rows for the traning sample 

set.seed(1889)
training.rows <- sample(1:n.row, tr*n.row, replace=FALSE)

#Assign to the training sample

#rownames(resultDF) = seq(length=nrow(resultDF))

train <- subset(SB[training.rows,])

## Assign the balance to the other two

int <- subset(SB[-c(training.rows),])

n.row <- nrow(int)

rownames(int) = seq(length=n.row)

int.rows <- sample(1:n.row, (ts/(ts+vd))*n.row, replace=FALSE)

# Assign the balance to the Test Sample

test <- subset(int[c(int.rows),])

vald <- subset(int[-c(int.rows),])
```
### Testing Equivalencies

```R{r}
options(width=60)

summary(train)
summary(test)
summary(vald)

round(mean(train$PetrolPrice),6)
round(mean(test$PetrolPrice),6)
round(mean(vald$PetrolPrice),6)

train$samp <- as.factor("train")
test$samp <- as.factor("test")
vald$samp <- as.factor("valid")

Combined <- rbind(train,test,vald)
head(Combined)

summary(aov(PetrolPrice ~ samp, data=Combined))
```


