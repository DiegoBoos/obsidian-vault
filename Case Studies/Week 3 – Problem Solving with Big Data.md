## **Key Learning Objectives**

- Understand **Data Engineering**: roles, responsibilities, and workflows.
- Explore **data collection requirements** and **architectural challenges**.
- Examine **sources of high-volume data** and **open data** principles.
- Learn about **Apache Kafka**, message brokers, and **stream processing**.
- Analyze the **FAIR principles** and **open licensing** issues.
- Compare open-source technologies used in big data ecosystems.
## **What is Data Engineering?**

Data Engineering involves:
- **Data ingestion & transformation** (e.g., rollups, metadata, exclusion for privacy).
- **Cataloging and storing data**.
- **Automation & orchestration** of data pipelines.
- **Security, access, and software development** tasks.
## **Requirements for Data Collection**

Includes:
- **Acquisition**: licenses, verifying, endpoints.
- **Labelling**: database schemas, naming.
- **Integration**: into models (ML, analytics).
- **Software tools**: for managing and maintaining data.
## **Sources of High-Volume Data**

1. **Public Data** – e.g., government open data portals.
2. **Private Data** – e.g., industry-generated (e-commerce, sensors).
3. **Data Exhaust** – system-generated (browsing history, GPS).
4. **Community Data** – social media, user-generated.
5. **Self-Quantification** – wearables, fitness apps.
## **Common Challenges in Big Data Architectures**

- **Data integrity issues**: e.g., missing values, incorrect transformations.
- **Scalability problems**.
- **Metadata issues**.
- **Human error and data corruption**.
## **Big Data Collection Approaches**

- Use **Distributed File Systems** (e.g., HDFS).
- Apply **compressed binary formats**:
    - Parquet, ORC, Avro.
- Utilize **Big Data SQL Engines**:
    - Hive, Impala, Presto.
## **FAIR Data Principles**

- **Findable** – searchable metadata.
- **Accessible** – no access barriers.
- **Interoperable** – format-independent (e.g., JSON, XML).
- **Reusable** – reusable under a clear license.
## **Open Data Licensing (Creative Commons)**

- **CC0** – No conditions.
- **CC-BY** – Requires attribution.
- **CC-NC** – Non-commercial use only.
- **CC-ND** – No derivative works.
## **Pros & Cons of Open Data**

**Pros**:
- Transparency, community engagement, reuse.

**Cons**:
- Misuse, privacy concerns, mosaic effects, cost of projects.
## **Big Data Tools & Ecosystem**

- **Open Source Ecosystem**: Spark, Hadoop, Kafka, Cassandra.
- **Message Brokers**: Kafka, Flume, Pulsar.
- **Stream Processors**: Spark, Storm, Flink.
## **Apache Kafka Overview**

- Functions as **message broker** and **stream processor**.
- Components:
    - **Zookeeper** – manages brokers.
    - **Brokers** – hold topic data.
    - **Producers & Consumers** – handle data input/output.
    - **Topics** – logical streams of data.

**Kafka Utilities**:
- **Kafka Streams** – Transformations.
- **Kafka Connect** – Source/Sink connectors (e.g., MongoDB, S3).
- **ksqlDB** – SQL for streaming queries.

Used often with **Docker** & **Docker Compose** for setup.
## **FAIR Practice Examples**

1. **Great Lakes Data** – not interoperable.
2. **Engine Stream** – FAIR if credentials available.
3. **Unfair Assignment** – violates Findable.
4. **Twitter/X** – no longer FAIR; closed off access.
## **Final Takeaways**

- Open data fosters **transparency** and **collaboration**.
- Data engineering is **foundational** to any big data workflow.
- **Kafka** is a crucial tool for real-time ingestion and processing.
- FAIR principles ensure data remains **usable and shareable**.
- Understand **licensing implications** before using or sharing data.