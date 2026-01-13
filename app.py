import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE

# 1. Data Load karna
try:
    df = pd.read_csv('patient_data.csv')
except FileNotFoundError:
    print("Pehle data_generator.py chalaein!")
    exit()

# 2. Preprocessing (Lab 1 & 2 Integration)
X = df.drop('Risk_Level', axis=1)
y = df['Risk_Level']

# Class Imbalance handle karna (SMOTE)
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Model Training (Lab 8 - Ensemble Model)
print("Training Random Forest Model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluation
y_pred = model.predict(X_test)
print("\n--- Project Evaluation ---")
print(classification_report(y_test, y_pred))

# 5. Visualization (Lab 10 - Explainability)
def plot_importance():
    importances = model.feature_importances_
    features = X.columns
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances, y=features)
    plt.title('Medical Feature Importance (Explainability)')
    plt.savefig('feature_importance.png')
    print("Graph saved as 'feature_importance.png'")
    plt.show()

if __name__ == "__main__":
    plot_importance()