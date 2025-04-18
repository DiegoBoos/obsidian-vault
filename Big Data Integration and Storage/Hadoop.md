Has two core components:
- HDFS
- MapReduce
	- Reliable and scalable storage solutions for big datasets
**MapReduce**
- A programming model developed by Google to facilitate distributed computation of large datasets
- Hadoop offers an open source version of MapReduce
- In Hadoop, when you start a job, mappers and reducers are running in the background
- You need “resources” to get jobs done
	- Nodes
	- CPU
	- Memory
- Hadoop uses YARN
	- MapReduce jobs negotiate with YARN to get resources for execution

**Commands**
**Create a directory:** hadoop fs -mkdir -p /BigData/hive
**Delete a file:** hadoop fs -copyFromLocal localFile /BigData/hive/.
**Delete a directory:** hadoop fs -rm -r /BigData/hive/retail_store_inventory
**Change permissions:** sudo hadoop fs -chmod -R 755 /BigData/hive/retail_store_inventory.csv