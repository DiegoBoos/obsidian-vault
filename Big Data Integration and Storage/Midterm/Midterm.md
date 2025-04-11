#### Name: Diego Bolaños
### ID: 8946481
# Step 1:  Single Node Kafka Broker Setup

## Prerequisites

- Java 8 or higher
- ZooKeeper (Kafka depends on ZooKeeper)
## 1. Download and Extract Kafka

```bash
# Download Kafka
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz

# Extract the archive
tar -xzf kafka_2.12-3.9.0.tgz
cd kafka_2.12-3.9.0
```
## 2. Start Zookeeper Server

```bash
cd zookeeper
bin/zkServer.sh start
```
## 3. Start Kafka Server

Following command should be executed under the Confluent directory

```bash
# Start Kafka Server
cd .. && cd confluent
bin/kafka-server-start etc/kafka/server.properties

nohup bin/kafka-server-start etc/kafka/server.properties > /dev/null 2>&1 &
```

## 4. Setup local and cluster connection

Go to GCP, and search for VM Instances, then copy the External IP
## 4. Create and Describe a Topic

- Need to specify where zookeeper is running
- Partitions is the number of partitions you want to create (you can have more than one partition per nod)
- Replication factor is set to 1 since we have one node (but usually 3 for replication factor)
```bash
bin/kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --topic my-news
```

Now run a describe command to get more details about the topic
```bash
bin/kafka-topics --describe --zookeeper localhost:2181 --topic my-news
```
## 5. Start consumer and producer

Need a list of few brokers (not all are necessary)  
Need to give topic name where producer will send messages

## 6. Create Console Producer

```bash
bin/kafka-console-producer --broker-list localhost:9092 --topic topic-name
```
## 7. Create Console Consumer

In a new terminal, start a consumer to read messages:

```bash
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic topic-name
```

![[Pasted image 20250323001445.png]]
# Step 2. Setup Kafka producer to ingest articles (V1)

![[Pasted image 20250322235554.png]]
![[Pasted image 20250322235625.png]]
![[Pasted image 20250322235654.png]]
Now we will have two new files
- **news_logfile:** This file will be in json format
![[Pasted image 20250323000535.png]]
- **news_csv:** This file will be in csv format, more suitable for running the hive queries
![[Pasted image 20250323000623.png]]
This file will have the headers which will be easier to save it in a hive table

However, the CSV transformation in the consumer script isn't properly handling the article data structure. I've found issues that difficult the readability of the dataset, such as the following:
1. The CSV format isn't properly separating fields
2. Raw HTML is being included without proper escaping
3. Content is being cut off showing the remaining characters
4. Records are not in a row format

To fix that we have to add data cleaning functions in the consumer as well so the consumer handles the data as they prefer

# Step 2. Setup Kafka producer to ingest articles (V2)

![[Pasted image 20250323212050.png]]
# Step 3: Setup a Kafka Consumer to read the data (V1)

![[Pasted image 20250322235730.png]]
# Step 3: Setup a Kafka Consumer to read the data (V2)

![[Pasted image 20250323212310.png]]
# Step 4: Use Apache Hive to gains insights

- Copy news data to HDFS, create Hive table, and run analysis

```bash
# Step 1: Create HDFS directory
hadoop fs -mkdir -p /BigData/news_data

# Step 2: Copy CSV file to HDFS
hadoop fs -copyFromLocal /home/siris837000638/midterm/articles.csv /BigData/news_data/.

# Step 3: Verify the file was loaded to HDFS
hadoop fs -ls /BigData/news_data/
```

- Type hive command

```bash
CREATE DATABASE news_db;
USE news_db;

CREATE EXTERNAL TABLE IF NOT EXISTS news_articles ( 
	source STRING, 
	author STRING, 
	title STRING,
	description STRING, 
	url STRING, 
	publishedAt STRING, 
	content STRING 
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
WITH SERDEPROPERTIES (
	"separatorChar" = ",", 
	"quoteChar" ="\"", 
	"escapeChar" = "\\" 
) 
STORED AS TEXTFILE 
LOCATION '/BigData/news_data' 
TBLPROPERTIES ('skip.header.line.count'='1');
```

***Query 1 Articles count by source***

```bash
SELECT source, COUNT(*) as article_count FROM news_articles GROUP BY source ORDER BY article_count DESC;
```

![[Pasted image 20250323211247.png]]
This query tells which sources contribute most to your dataset

***Query 2 Articles published per day*** 

```bash
SELECT publishedAt as publication_date, COUNT(*) as daily_article_count FROM news_articles GROUP BY publishedAt ORDER BY publishedAt DESC;
```
![[Pasted image 20250323211307.png]]
This query shows publishing patterns over time

***Query 3 Author publishing***

```bash
SELECT author, COUNT(*) as article_count, COUNT(DISTINCT source) as source_count FROM news_articles GROUP BY author ORDER BY article_count DESC;
```

![[Pasted image 20250323211408.png]]
This query identifies the authors that publishes the most and also distinct if there is multiple sources

