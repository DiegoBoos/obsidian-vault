Some problems require iterative processing using a set of instructions or a MapReduce job ***multiple times*** to get the expected output
- Logistic regression, interactive data mining, etc

**Example: machine learning process**
Machine learning is nothing more than non-linear optimization
- Take a cost function and find the minimum
- This is an iterative process like gradient descent

**Hadoop problems**
Reading first input and writing the final output to HDFS is unavoidable
- You have to save the data somewhere!
- But we do two intermediate reads and writes
- Intermediate reads and writes are inefficient
- 50 GB intermediate input/output take a lot of time = slow execution time
- Iterations compound the problem

**Spark solution**
- Keep the intermediate data in memory
- NOT a ground breaking thing, all applications in fact do this
-  Spark is able to do in-memory processing plus fault tolerance
- Can’t just “replicate” memory unlike hard disk

**Summary**
- Spark’s main breakthrough was appreciating that there are many problems in Big Data where you are repeatedly reading and writing data into hard disk
- Traditional hard disk distributed storage has a lot of overhead
- So it sped things up by saving intermediate data in memory and making it fault tolerant