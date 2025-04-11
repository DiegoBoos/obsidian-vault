## Lecture Focus: Parallel Processing in Big Data

### What is Parallel Processing?

- Divides a task across **two or more microprocessors**.
- Designed for **complex tasks** to be broken into subtasks, processed concurrently.
- Used in tools like **Hadoop** to enable **parallel and distributed processing**.
- Example: A supercomputer analyzes data from weather stations, satellites, and soil samples **simultaneously** to optimize crop planting.
### Advantages of Parallel Processing:

1. **Speed**: Multiple bits sent at once → higher data transfer rates.
2. **Simpler Hardware**: Requires fewer complex electronics.
3. **Scalability**: Add more nodes as data grows without performance drop.
### Disadvantages of Parallel Processing:

- **Communication Overhead**: Synchronization between nodes introduces delays.
- **Limited Use Cases**: Not suited for interdependent tasks.
- **Distance Limitations**: Works best over short distances.
- **Synchronization Issues**: Requires precise timing.
### Historical and Modern Trends

- Began with **ILLIAC IV (1960s)** – first supercomputer using SIMD (Single Instruction Multiple Data).
- Modern supercomputers use **MIMD DMMP** (Multiple Instructions, Multiple Data with Distributed Memory and Message Passing).
- Performance measured in **FLOPS** (Floating-Point Operations per Second).
- Current targets: **ExaFLOPS (10¹⁸)** performance levels.
### Key Parallel Processing Models:

- **Data Parallelism**:
    - Splits large data into chunks processed in parallel.
    - Works well when applying **same operations** to each chunk.
- **MapReduce (Google)**:
    - `Map`: processes chunks individually.
    - `Reduce`: aggregates key-value pairs.
- **Apache Spark**:
    - Unified engine for ETL, ML, SQL, streaming.
    - Uses **RDDs** (Resilient Distributed Datasets) for efficiency.
### Data Parallel Architecture – Pros & Cons:

**Pros:**
- **High scalability**
- **Performance gains** with less data movement
- **Simplified logic**

**Cons:**
- **Overhead** from node communication
- **Limited to simple, uniform operations**
### Mapping, Scheduling, and Virtualization

- **Mapping**: Assigning computations to hardware → ideally automatic.
- **Scheduling**: Assigns tasks to nodes under constraints (e.g. deadline, energy).
- **Virtualization**:
    - Protects and isolates users.
    - Enhances reliability.
    - Hides hardware complexity.
### Tools
#### Apache Spark
- Unified analytics engine (in-memory)
- Fast for:
    - **Batch processing**
    - **Streaming**
    - **SQL**
    - **Graph computations**
    - **ML**
#### Apache Impala
- MPP SQL engine for Hadoop
- **Low-latency** SQL queries
- Faster than Spark for **ad-hoc queries**
- Ideal for **relational BI on Hadoop**
### Chapter Summary
- Parallel Processing: definition, benefits, drawbacks
- Data Parallelism architecture
- Key models: **SIMD, MIMD, MapReduce, Spark**
- Scheduling, virtualization
- **Tools**: Apache Spark, Apache Impala
