Data analysis requires organizing and modeling data in ways that enable statistical or machine learning methods. Most techniques demand **structured or semi-structured data**, even when original sources are unstructured.
## 🧱 Types of Data Structures

### 🔷 Rectangular Data Structures (Most Common)

- The standard form: **tables with rows (records) and columns (features/variables)**
    
- Equivalent to **data frames**, **spreadsheets**, or **relational database tables**
    
- Required for most analytical and statistical techniques
#### 📘 Glossary

| Term       | Definition                                    | Synonyms                               |
| ---------- | --------------------------------------------- | -------------------------------------- |
| Data Frame | Table of variables and values, often indexed  | Basic unit for data science & ML       |
| Feature    | A column in the data table                    | Variable, attribute, predictor, input  |
| Outcome    | Target variable (often to predict or explain) | Dependent variable, label, response    |
| Record     | A row in the data table                       | Instance, observation, example, sample |
### 🔶 Non-Rectangular Data Structures

These are increasingly common in modern "big data" contexts and require special handling.

| Type              | Key Features                                                               | Common Use Cases                             |
| ----------------- | -------------------------------------------------------------------------- | -------------------------------------------- |
| **Time Series**   | Repeated measures over time                                                | Forecasting, sensors, stock prices           |
| **Spatial Data**  | Includes coordinates, either object-based (e.g., landmarks) or field-based | Mapping, geolocation, environmental analysis |
| **Graph/Network** | Represents relationships (e.g., social networks, logistics)                | Network optimization, recommender systems    |
### 🔶 Structured vs Unstructured Data

|Type|Description|Examples|
|---|---|---|
|**Structured**|Organized in pre-defined schema (RDBMS, spreadsheets)|Customer records, sales tables|
|**Semi-Structured**|Some pattern present for parsing|XML, JSON, log files|
|**Quasi-Structured**|Pattern is inconsistent, needs cleanup|Web clickstream data|
|**Unstructured**|No predefined format|Text, PDFs, images, videos|
## 🔢 Types of Variables

Understanding variable types is crucial for choosing the right analysis method.
### 🔷 Categorical Variables

| Type        | Description                      | Examples                 | Synonyms            |
| ----------- | -------------------------------- | ------------------------ | ------------------- |
| Nominal     | Categories without order         | Hair color, city names   | Factors, enumerated |
| Dichotomous | Two possible values              | Yes/No, True/False       | Boolean, binary     |
| Ordinal     | Categories with a specific order | Survey: Agree → Disagree | Ordered factors     |

### 🔷 Numerical Variables

| Type       | Description                                     | Examples           | Synonyms     |
| ---------- | ----------------------------------------------- | ------------------ | ------------ |
| Discrete   | Countable integer values                        | Number of siblings | Counts       |
| Continuous | Real numbers within a range                     | Height, weight     | Float        |
| Interval   | Numeric values where zero has no "true" meaning | Temperature (°C)   | Linear scale |
| Ratio      | Like interval, but zero means “none”            | Distance, weight   | True zero    |
## 📈 Importance of Structuring

- **Machine learning models** like logistic regression, decision trees, and SVMs rely on **rectangular structures**
    
- **Unstructured data** (text, images) must be transformed (e.g., through NLP or computer vision pipelines)
    
- **Data wrangling and transformation** are critical steps before model training
