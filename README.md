# HealthGuard AI: Interpretable Medical Triage & Risk Assessment

## 📌 Project Overview
This project is a comprehensive Machine Learning application developed for **Lab 14 (Complex Computing Activity)**. The system acts as a clinical decision support tool that classifies patients into three risk categories (Low, Medium, High) based on real-time vital signs.

Unlike "black-box" models, this system focuses on **Explainability (XAI)**, allowing medical professionals to see exactly which features (like Oxygen Saturation or Blood Pressure) influenced a specific risk prediction.

## 🛠 Lab Integrations (1-12)
As per the requirements of the CCA, the following concepts were integrated:
* **Lab 1 & 2 (Preprocessing):** Handling data distribution, feature scaling using `StandardScaler`, and addressing class imbalance via `SMOTE`.
* **Lab 8 (Ensemble Learning):** Implementation of a `RandomForestClassifier` to handle non-linear clinical data.
* **Lab 10 (Model Interpretation):** Feature importance visualization to ensure clinical transparency.

## 📁 Project Structure
- `data_generator.py`: Script to synthesize clinical EMR data.
- `app.py`: Main engine for training, evaluation, and visualization.
- `patient_data.csv`: The generated dataset.
- `feature_importance.png`: Visual proof of model's decision-making logic.

## 🚀 How to Run
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/santoshkumar129/Predictive-Medical-Analytics.git)
   
