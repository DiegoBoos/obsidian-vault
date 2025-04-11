Regression/Prediction – To fit a continuous value, such as Goals Against Average or Salary
Classification – To predict a categorical outcome, such as ‘Above Average’ or ‘Success/Failure’

But why bother?
1. Problems often require an automated decision.
2. Often problems have binary outcomes.
3. Classification represents the most common sort of data analysis problem.

Examples of Classification problems:
- Is an email an attempt at phishing? (phishing/not-phishing)
- Is a customer likely to churn? (churn/don’t churn)
- Is the web user likely to click on an advertisement? (click/don’t click)

Often, we need more than a simple binary classification: we want to know the predicted probability that a case belongs to a class.

Rather than having a model simply assign a binary classification, many algorithms can return a probability score (propensity) of belonging to the class of interest.

A sliding cutoff can then be used to convert the propensity score to a decision. The general approach is as follows:
1. Establish a cutoff probability for the class of interest above which we consider a record as belonging to that class.
2. Estimate (with any model) the probability that a record belongs to the class of interest. 
3. If that probability is above the cutoff probability, assign the new record to the class of interest.

- E.g. GAA > 2.85 = 1 (“High”), GAA <= 2.85 = 0 (“Low")