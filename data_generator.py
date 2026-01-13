import pandas as pd
import numpy as np

def create_dataset():
    np.random.seed(42)
    n_samples = 1500
    data = {
        'Age': np.random.randint(18, 85, n_samples),
        'Systolic_BP': np.random.randint(90, 180, n_samples),
        'Oxygen_Saturation': np.random.randint(80, 100, n_samples),
        'Heart_Rate': np.random.randint(50, 130, n_samples),
        'Body_Temp': np.random.uniform(96, 105, n_samples),
        # Risk: 0=Low, 1=Medium, 2=High
        'Risk_Level': np.random.choice([0, 1, 2], n_samples, p=[0.6, 0.3, 0.1])
    }
    df = pd.DataFrame(data)
    df.to_csv('patient_data.csv', index=False)
    print("Dataset 'patient_data.csv' successfully created!")

if __name__ == "__main__":
    create_dataset()