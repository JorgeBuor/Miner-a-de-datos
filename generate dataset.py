import pandas as pd
import numpy as np

np.random.seed(42)
n = 550

# --- Base variables ---
age = np.random.randint(16, 30, n).astype(float)
gender = np.random.choice(['Male', 'Female', 'Other'], n, p=[0.48, 0.49, 0.03])
city_origin = np.random.choice(['Barranquilla', 'Bogotá', 'Medellín', 'Cali', 'Other'], n, p=[0.35, 0.25, 0.15, 0.10, 0.15])
hs_gpa = np.round(np.random.uniform(2.5, 5.0, n), 2)
admission_score = np.round(np.random.uniform(200, 500, n), 1)
first_sem_gpa = np.round(np.random.uniform(1.5, 5.0, n), 2)
socioeconomic_level = np.random.choice([1, 2, 3, 4, 5, 6], n, p=[0.20, 0.25, 0.25, 0.15, 0.10, 0.05])
scholarship = np.random.choice(['Yes', 'No'], n, p=[0.30, 0.70])
loan = np.random.choice(['Yes', 'No'], n, p=[0.40, 0.60])
financial_aid = np.random.choice(['Yes', 'No'], n, p=[0.25, 0.75])

# --- Dropout logic (realistic weights) ---
dropout_prob = (
    0.4 * (first_sem_gpa < 3.0).astype(float) +
    0.2 * (socioeconomic_level <= 2).astype(float) +
    0.15 * (scholarship == 'No').astype(float) +
    0.1 * (hs_gpa < 3.5).astype(float) +
    0.1 * (admission_score < 300).astype(float) +
    0.05 * (loan == 'No').astype(float)
)
dropout_prob = np.clip(dropout_prob / dropout_prob.max(), 0.05, 0.95)
dropout = np.where(np.random.rand(n) < dropout_prob, 'Yes', 'No')

df = pd.DataFrame({
    'age': age,
    'gender': gender,
    'city origin': city_origin,
    'hs gpa': hs_gpa,
    'admission score': admission_score,
    'first sem gpa': first_sem_gpa,
    'socioeconomic level': socioeconomic_level,
    'scholarship': scholarship,
    'loan': loan,
    'financial aid': financial_aid,
    'dropout': dropout
})

# --- Nulls (random ~5% per column) ---
null_cols = ['age', 'hs gpa', 'admission score', 'first sem gpa', 'socioeconomic level']
for col in null_cols:
    null_idx = np.random.choice(df.index, size=int(n * 0.05), replace=False)
    df.loc[null_idx, col] = np.nan

# --- Outliers ---
outlier_idx = np.random.choice(df.index, size=15, replace=False)
df.loc[outlier_idx[:5], 'age'] = np.random.choice([5, 65, 70], 5)
df.loc[outlier_idx[5:10], 'hs gpa'] = np.random.choice([0.5, 5.8, 6.2], 5)
df.loc[outlier_idx[10:], 'first sem gpa'] = np.random.choice([0.2, 5.9, 6.5], 5)

df.to_csv('student dropout dataset.csv', index=False)
print(f"Dataset generated: {len(df)} records")
print(df.dtypes)
print(f"\nDropout distribution:\n{df['dropout'].value_counts()}")
print(f"\nNull counts:\n{df.isnull().sum()}")
