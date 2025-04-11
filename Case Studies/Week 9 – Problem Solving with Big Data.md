## Lecture Overview – Week 9

### Objectives

- Revisit six elements of a big data project.
- Understand data processing and cleansing.
- Learn about validation, monitoring, and Hadoop metrics.
- Discuss common pitfalls in big data systems.
## Six Elements of a Big Data Project

1. **Data Research & Integration**
    - Focus on provenance & integration points.
    - Requires revision after deeper data inspection.
2. **Data Collection**
    - Continuous or periodic.
    - Begin with test data; explore suitable tools.
3. **Data Storage & Maintenance**
    - Must address long-term and regulatory needs.
    - Choose appropriate storage platforms (e.g., NoSQL, Hadoop).
4. **Data Quality**
    - Ensures accuracy and consistency across sources.
5. **Data Analysis & Visualization**
    - Derive value and insights from data.
6. **DevOps**
    - Integrates tools like GitHub to support agile development.
## Data Processing

### What is it?
- Transforming raw data into actionable formats (collect, filter, sort, analyze).
- Ensures data is accurate, valid, and supports decision-making.
### Why Important?

- Avoids errors, improves reliability, and speeds up processes.
- Encourages documented processes to ensure consistency and reduce disruptions.
## Data Cleansing

1. **Import Unclean Data** from various systems.
2. **Monitor Data Flows** – Use control charts, Bland-Altman plots.
3. **Standardize Processes** – Ensure repeatability and adaptability.
4. **Merge Datasets** – From CSV, SQL, Excel, SAP, etc.
5. **De-Duplicate** – Identify and manage duplicate records.
6. **Standardize Values** – Handle casing, extra spaces, phone/email formatting, etc.
## Data Validation Steps
- Validate against internal/external sources.
- Communicate clearly with teams.
- Track processing time and cost for efficiency.
## Monitoring & Service Levels

- **SLO (Objectives)** – E.g., Mean time to repair, avg response time.
- **SLA (Agreements)** – Formal commitments, internal or external.
- Tools & templates: [slatemplate.com](https://slatemplate.com/), [slatools.com](https://slatools.com/)
### Alerting
- Set up alerts for:
    - High CPU/memory
    - 100% disk usage
    - Downtime thresholds (e.g., 99% uptime = 3.65 days/year)
## What Could Possibly Go Wrong?

- Hardware issues: disks, RAM, fans, network cards
- Networking: cable issues, overflows, upgrades
- Software: corruption, bugs, memory leaks, cyber attacks
- Human errors (e.g., misconfiguration)
## Key Hadoop Metrics

- **HDFS Metrics**
    - NameNode: missing blocks, capacity remaining.
- **MapReduce Counters**
    - Job/task level stats.
- **YARN Metrics**
    - Active/unhealthy nodes.
- **ZooKeeper Metrics**
    - Latency, availability.
## Chapter Summary
You should now be confident with:
- End-to-end lifecycle of big data projects.
- Techniques for data processing and cleansing.
- Methods for validating and monitoring.
- Identifying failure points and using Hadoop performance metrics.