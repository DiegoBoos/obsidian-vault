- Is Spark a replacement for Hadoop? Or is Hadoop “dying”?
	- No
- Spark enhances the Hadoop stack and is not meant to replace it
	- It enhances the speed of computations
- Spark is a great tool for Data Analysts using PIG or HIVE
	- Use Spark for faster execution times

I already have a bunch of jobs that were implemented in traditional Hadoop MapReduce, should I implement them in Spark?
- Depends, if you are creating new jobs look at Spark even ifyour speed needs are met
- Generally not recommended to convert all your current jobs to Spark Jobs
	- Look at the slow ones and migrate them to Spark
- Hard to ignore 10x speed improvement

**Summary**
- Power of Spark lies in its computational speed
- Its execution engine is faster than Hadoop’s MapReduce implementation
- Spark is designed to work on top of Hadoop leveraging YARN and HDFS
- 10x (at least) speed improvement is quite compelling and you see quite a bit of traction with Spark now