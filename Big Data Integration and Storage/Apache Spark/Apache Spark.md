**Spark website**: http://spark.apache.org/
### Taglines
- “Lightning fast cluster computing”
- “Spark is a fast and general engine for large-scale data processing”
### Tagline Now:
- “Unified engine for large-scale data analytics”

Spark is an execution engine that can do fast computations on big datasets
- Example: average volume by stock symbol on a stock dataset
- Write a few lines of code (Scala, Python or Java)
- Spark will spin up the tasks on different machines on your cluster and give your results very fast
### Apache Spark Speed
- “Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.“
- 100x faster than hadoop
### Spark
1) **Storage**
	- Spark does not offer a big data storage solution
	- What is the difference between Big Data Storage and regular storage? The whole concept of replication, keeping track of pieces of your data etc, in short there is no “HDFS”
	- Spark leverages existing distributed file systems like Hadoop’s HDFS or Cloud services like Amazon S3 or big data databases like HBase, Cassandra, etc
2) **Computation method**
	 - False misconception 
		- “Spark job executions are fast because it does not use the MapReduce model”
	- Spark’s goal is not to find an alternative to MapReduce
		- We still have map, reduce, shuffle
	- Spark replaces Hadoop’s implementation of MapReduce with its own implementation
		- Faster and more efficient
	- Spark replaces Hadoop’s implementation of MapReduce with its own implementation
		- Faster and more efficient
	- The stages in MapReduce are the same in both technologies
3) **Computational Speed**
	- The 100x improvement only true for certain cases only
		- Example logistic regression
		- Keep doing the same computation on different outputs
	- Spark speeds things up by keeping output in memory (among other things)

4) **Resource management**
- Same thing applies to Spark, it needs to look for resources
- Spark however has its own in-built resource manager
	- So we don’t need YARN
- But we can request that Spark use YARN as the resource manager

**Starting spark:** spark-shell --master yarn

```scala
import org.apache.spark.sql.SparkSession

val hiveSession = SparkSession.builder()
.appName("Hive to Spark Example")
.config("spark.sql.warehouse.dir", "/user/hive/warehouse")
.enableHiveSupport()
.getOrCreate()

val stocksDF = hiveSession.sql("SELECT * FROM stocks_db.stocks")
stocksDF.show(5)
```

  
val schema = new StructType()  
.add("Date", "date")  
.add("storeID", "string")  
.add("productID", "string")  
.add("Category", "string")  
.add("Region", "string")  
.add("Inventory Level", "int")  
.add("Units Sold", "int")  
.add("Units Ordered", "int")  
.add("Demand Forecast", "double")  
.add("Price", "double")  
.add("Discount", "int")  
.add("Weather condition", "string")  
.add("Holiday Promotion", "int")  
.add("Competition pricing", "double")  
.add("Seasonality", "string")
```