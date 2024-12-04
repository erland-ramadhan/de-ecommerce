# ETL case

## Objective
Design and implement a robust ETL (Extract, Transform, Load) pipeline that demonstrates your data engineering skills, problem-solving abilities, and understanding of modern data processing techniques.

## Scenario
You are a data engineer at a fast-growing e-commerce company. The business needs a flexible ETL pipeline to process and analyze sales data from multiple sources.

## Technical Requirements

### 1. Data Sources
Develop an ETL pipeline that can handle:
- **Primary Source**: CSV file with sales transaction data
- **Secondary Source**: JSON API endpoint with product information
- **Optional Advanced Source**: Simulated real-time data stream

#### Sample Data Structure
**Sales Transaction CSV**:
- transaction_id
- customer_id
- product_id
- sale_date
- quantity
- total_price
- sales_channel

**Product API Endpoint**:
- product_id
- product_name
- category
- manufacturer
- base_price

### 2. Transformation Requirements
Implement complex transformations including:
- Data cleaning and normalization
- Handling missing or inconsistent data
- Calculating derived metrics:
  - Total revenue per product
  - Sales performance by channel
  - Customer purchase frequency
  - Inventory valuation

### 3. Technical Constraints
- Use Python as the primary language
- Implement modular, reusable code
- Include comprehensive error handling
- Provide logging and monitoring capabilities (monitor using tools such as prometheus, grafana)

## Deliverables

### 1. Source Code
- Complete ETL pipeline implementation
- Modular design with clear separation of concerns
- Well-documented functions and classes

### 2. Data Transformation Logic
- Demonstrate advanced pandas or PySpark transformations
- Show ability to handle complex data manipulation
- Implement data validation techniques

### 3. Orchestration
- Use Apache Airflow or Prefect to create a workflow
- Define clear DAG (Directed Acyclic Graph)
- Implement retry and error handling mechanisms

### 4. Deployment
- Dockerized solution
- `docker-compose.yml` for easy setup
- Clear instructions for local and cloud deployment

## Evaluation Criteria

### Technical Proficiency (40 points)
- Code quality and maintainability
- Efficient data transformation logic
- Error handling and data validation
- Performance optimization techniques

### Architecture and Design (30 points)
- Modular and scalable pipeline design
- Separation of concerns
- Workflow orchestration
- Extensibility of the solution

### Data Engineering Skills (20 points)
- Complex transformation capabilities
- Handling of real-world data challenges
- Understanding of data cleaning techniques
- Derived metric calculations

### Documentation and Deployment (10 points)
- Clear README
- Docker configuration
- Setup and run instructions
- Explanation of design choices

## Bonus Challenges (Optional)
- Create a simple dashboard or visualization
- Implement advanced data quality checks
- Setup CI/CD pipeline

## Submission Guidelines
1. Detailed README.md explaining:
   - Architecture overview
   - Setup instructions
   - Design rationale
   - Performance considerations
2. Provide instructions for running the pipeline

## Technical Stack Recommendations
- Language: Python 3.8+
- Data Processing: Pandas, PySpark
- Orchestration: Apache Airflow, Prefect, Mage
- Containerization: Docker
- Databases: PostgreSQL, SQLite, etc
- Optional: Great Expectations for data validation

## Assessment Goals
We are evaluating:
- Technical problem-solving skills
- Data engineering expertise
- Code quality and maintainability
- Understanding of modern data processing techniques

## Confidentiality
- Treat this challenge as confidential
- Do not share the assessment publicly
- Focus on demonstrating your unique approach