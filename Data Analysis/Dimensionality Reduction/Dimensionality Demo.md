```R{r}
##################################################
### PROG8435                                    ##
### Data Reduction Demonstration                ##
### Demonstration                               ##  
##################################################
#                                               ##
##################################################

# Written by David Marsh
# ID: 123456789
#

##############################
## Read in Data             ##
##############################

options(digits=5)
Master <- read.csv("PROG8435_Dimension_Data_Demo.csv", header = TRUE, sep = ",")
head(Master)

start <- Sys.time()
cor(Master,method="spearman")
end <- Sys.time()
Tot1 <- end-start
Tot1

##############################
## Reduce Number of Vars    ##
##############################

# Find missing values
# Identify cols > 99% missing
summary(Master)

#Look like X02 is likely!
Master <- Master[-c(3)]
head(Master,8)

# Identify Low Variance
stat.desc(Master)  #Consider coef of var
summary(Master)

#Based on the above X04 seem likely. Let's check!
table(Master$X04)
Master <- Master[-c(4)]
head(Master,7)

#Identify High Correlation
round(cor(Master,method="spearman"),3)

#X05 and X06 seem highly correlated
#Don't need to keep both, I'll drop the second one.

Master <- Master[-c(5)]
head(Master,3)
Master <- Master[-c(1)]
head(Master)

start <- Sys.time()
cor(Master,method="spearman")
end <- Sys.time()
Tot2 <- end-start
Tot2

Tot1
Tot2