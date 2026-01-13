# 🏥 Lab 14: Complex Computing Activity (CCA)
## Project Title: AI-Driven HealthGuard: End-to-End Medical Triage & Interpretability System

---

### 📋 Project Overview
This project is developed as the final **Complex Computing Activity (LAB #14)**. It demonstrates the end-to-end mastery of Machine Learning pipelines—from synthetic data generation and advanced preprocessing to model deployment and explainability.

In high-pressure clinical environments, prioritizing patients (Triage) is critical. **HealthGuard AI** automates this by classifying patient risk levels while providing "Why" behind every prediction, ensuring transparency for medical practitioners.

---

### 🧬 Integrated Lab Concepts
To satisfy the requirements of Lab 14, this project integrates the following core concepts from the curriculum:

Concept,Lab No.,Implementation in Project
Data Preprocessing,Lab 01,Used StandardScaler for normalization and SMOTE for handling class imbalance.
Random Forest,Lab 05,Applied as the main classification engine for robust predictions.
K-Means Clustering,Lab 10,Used to group similar patient profiles and detect anomalies in health data.
---

### 🏗 System Architecture
The pipeline follows a modular structure:
1. **Ingestion:** `data_generator.py` creates a 1500-sample EMR dataset.
2. **Processing:** Cleaning, scaling, and balancing the dataset.
3. **Intelligence:** Training the Random Forest ensemble model.
4. **Insight:** Generating visual interpretability reports.



---

### 🚀 Getting Started

#### 1. Clone the Repository
```bash
git clone [https://github.com/santoshkumar129/Predictive-Medical-Analytics.git](https://github.com/santoshkumar129/Predictive-Medical-Analytics.git)
cd Predictive-Medical-Analytics
2. Environment Setup
Install the necessary dependencies:

Bash

pip install -r requirements.txt
3. Execution Flow
Generate the clinical data first, then run the analytical engine:

Bash

python data_generator.py
python app.py
📊 Performance & Ethics
Metrics: Evaluation via Precision-Recall curves and Confusion Matrices to minimize 'False Negatives' in High-Risk cases.

Ethics: Designed with fairness in mind, avoiding biased demographic features and focusing strictly on clinical vitals.

🔗 Reference & Links
GitHub Repository: Predictive-Medical-Analytics

Lab Course: Machine Learning / Complex Computing Activity (Lab #14)

Developed as a part of the academic requirement for Lab 14.
