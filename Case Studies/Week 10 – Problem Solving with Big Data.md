## **Key Concepts & Summary from Week 10**

### Six Elements of a Big Data Project

1. **Data Research & Integration**  
    – Ensure provenance and integration points.  
    – Revisit as deeper analysis occurs.
2. **Data Collection**  
    – Continuous process (e.g., real-time or periodic).  
    – Begin with test data collection.
3. **Data Storage & Maintenance**  
    – Consider regulatory needs and tools (e.g., DBs).  
    – Decide: _Where_ to store and _what_ to use.
4. **Data Quality**  
    – Focus on tracking and maintaining data accuracy/reliability.
5. **Data Analysis & Visualization**  
    – Main value point of big data projects.
6. **DevOps**  
    – Integrate tools like GitHub to accelerate development.
### **Private vs Public Cloud**
#### Private Cloud
- Hosted internally (Enterprise DC or Virtualized via OpenStack/Vmware).
- Greater control, but expensive infrastructure.
#### Public Cloud
- Providers: AWS, GCP, Azure, etc.
- Easier scalability, lower initial cost, but may lead to higher long-term costs and vendor lock-in.
### **Case Study: Liberty Mutual**
- Needs: 1PB storage, 1TB/day growth, 16-core servers.
- **Private Cloud**: $900k–$1M in hardware + other infra costs.
- **Public Cloud (GCP)**: Calculated via [Google Cloud Calculator](https://cloud.google.com/products/calculator/).
### **Cloud Solutions Compared**

|Model|Pros|Cons|
|---|---|---|
|**Unmanaged**|Cheaper infra|Higher total cost & management overhead|
|**Managed Cloud**|Flexibility in control vs outsourcing|May be costly or complex to manage|
|**Fully Outsourced**|Focus on business, low maintenance|Expensive, less flexibility|
### **Google Cloud Platform (GCP) – Overview**
- Services: Compute, Storage, Data Analytics, ML.
- Infrastructure: SaaS, PaaS, IaaS.
- Part of Google Workspace (Gmail, Docs, etc).
#### Why GCP?
- Strong in **data analytics**, **ML**, **serverless**.
- **Open-source**, **hybrid-cloud friendly**.
- Pay-per-second billing.
#### How GCP Works
- Projects manage settings, permissions, and metadata.
- Access via Console (GUI), CLI, or APIs.
### **Cloud Providers Comparison**

| Provider  | Strengths                                        | Limitations                                     |
| --------- | ------------------------------------------------ | ----------------------------------------------- |
| **Azure** | Hybrid integration, enterprise friendly          | Complexity, vendor lock-in                      |
| **AWS**   | Global reach, compliance support                 | Complex billing, regional limits                |
| **GCP**   | Data/ML strengths, fast network, Kubernetes lead | Fewer services, security concerns for some orgs |
### **Top Cloud Computing Challenges & Solutions**

| Challenge              | Solution                                    |
| ---------------------- | ------------------------------------------- |
| Data security/privacy  | MFA, antivirus, firewalls, visibility tools |
| Multi-cloud complexity | Software updates, patch management          |
| Performance dependency | Real-time monitoring tools                  |
| Interoperability       | Standardize tools & workflows               |
| Network outages        | Pay for higher bandwidth, optimize infra    |
| Skills shortage        | Hire experts or train internally            |
| Password security      | Use password managers & MFA                 |
| Hidden costs           | Monitor resources, audit regularly          |
| Governance issues      | Align IT operations with cloud strategy     |
| Compliance gaps        | Apply GDPR and industry frameworks          |
### **Tips for Exam Prep from this Lecture**

- Understand **advantages and disadvantages** of different cloud models.
- Memorize **GCP's role and tools** for big data projects.
- Be able to **justify cloud solutions** based on specific business needs (e.g., cost vs performance).
- Know the **six key components** in managing big data projects.
- Review **case studies** (e.g., Liberty Mutual) for practical application of infrastructure planning.