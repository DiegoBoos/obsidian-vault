
| Model          | Outcome                      |
| -------------- | ---------------------------- |
| Regression     | Continuous                   |
| Clustering     | Groups                       |
| Classification | Categorical (usually binary) |
Final Review #1

Rel.Comp ++
Sur.Area --
Well.Area +
Rf.Area ---
Or.Height +++
Orient o+
Glaz.Area +
Glaz.Area.Dst o+
COnst.comp 0-

Roof.Area 

| Height     | Surface.Area |
| ---------- | ------------ |
| Regression | Components   |

| Surface    | Height  |
| ---------- | ------- |
| Regression | Compact |

| Height | Compact |
| ------ | ------- |

Anything you did on the training set you have to do to the test set when you test it

1. Plan (Define the problem)
2. Look at the data describe it
	1. Read it in
	2. Summary Measures (Mean, Var)
	3. Graphical Summaries (eg. Density, histograms)
3. Transformation/Reduction
4. Split into Test set (validate the model)/ Train set (Build the model)
5. Correlations/Interactions (E.g. Correlation Matrices, Scatter Plots, etc)
6. Build Model
	1. Clustering - K-means
	2. Regression - Linear regression (with selection)
	3. Classification 
		1. Logistic regression (glm)
		2. N-B
		3. NN 
		4. RCP
	4. ROC (Associated Calculations)
	5. Confusion Matrices (Calcs)
7. Assess/ Validate/ Refine the Model
8. Apply the Model
	1. New Dataset
	2. Write out File