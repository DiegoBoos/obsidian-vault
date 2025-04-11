## **Key Topics Covered**

### **1. Data Management: Importance & Tools**

- **Purpose**: Encompasses collecting, processing, storing, analyzing, and sharing data.
- **Tools Include**:
    - Library systems (for acquisition, organization, and circulation)
    - Libraries as data custodians (print + digital).
### **2. Six Main Elements of a Big Data Project**

1. **Data Research & Integration**
2. **Data Collection** (real-time or scheduled)
3. **Data Storage & Maintenance** (long-term, regulatory)
4. **Data Quality** (accuracy, consistency)
5. **Data Analysis & Visualization** (derive value)
6. **DevOps** (tools like GitHub to speed up development).
### **3. Core Data Management Systems**

- **CRM**: Manages customer interactions and data.
- **Marketing Tech**: Tools for email, campaign management.
- **Data Warehouses**: Stores product usage & satisfaction metrics.
- **Analytics Tools**: BI, visualizations, reporting for decision-making.
### **4. Best Practices in Data Management**

- **Data Tiering**: Store data efficiently and reduce redundancy.
- **Pipeline Management**: Clean and prepare data during ingestion.
- **Federation**: Access from anywhere (on-prem/cloud).
- **Discoverability**: Make data easy to find and reuse.
### **5. Key Concepts: Database vs Data Lake vs Warehouse**

|Feature|Database|Data Lake|Data Warehouse|
|---|---|---|---|
|Workload|Transactional|Analytical|Analytical|
|Schema|Rigid or flexible|No schema (schema-on-read)|Predefined schema (on-write)|
|Data Type|Structured/semi|Structured/unstructured|Structured/semi|
|User|Developers|Data scientists, analysts, devs|Analysts, data scientists|

- **Pros and Cons** explained for all three types.
### **6. Hardware for Big Data**

- **Server Components**: CPUs, RAM, SSD/HDD, Network Interface Cards.
- **Server Rack Benefits**: Cooling, power distribution, scalability, security.
- **Data Center**: Houses critical infra like switches, storage, firewalls.
### **7. CAP Theorem**

- In distributed systems, you can only guarantee **two** of:
    - **Consistency**
    - **Availability**
    - **Partition Tolerance**.
### **8. Resource Planning**

- Estimate based on:
    - **4–8GB RAM per core**
    - **1–2 disk spindles per core**
    - Evaluate if workloads are CPU or I/O intensive.
### **9. Insurance Company Use Case**

- **Scenario**: Freedom Mutual plans a Hadoop cluster.    
- **Needs**: 1PB storage, 1TB/day growth, on-site center.
- **Calculation**:
    - 12×8TB disks/server → ~40 servers for replication & overhead.
    - Add new server every 20–25 days.
- **High Availability**: Replicas on separate racks, zone & region replication, RPO/RTO planning.
### **10. Summary**

The life cycle of big data management:
- **Collection** → **Storage** → **Query/Retrieval** → **Usage/Analysis** → **Archival/Retirement**