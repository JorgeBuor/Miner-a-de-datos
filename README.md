# Student Dropout Prediction — Synthetic Dataset

This dataset was created as part of Activity I for the Data Mining course at Universidad de la Costa. It simulates real-world student data to predict whether a student will drop out during their first academic year using Machine Learning classification models.

---

## Repository Structure
```
├── student dropout dataset.csv   # Synthetic dataset (550 records)
├── generate dataset.py           # Python script used to generate the dataset
└── README.md                     # Dataset documentation
```

---

## Problem Statement

Universities face high dropout rates in undergraduate programs. The goal is to build a system that can identify, early on, which students are at greater risk of dropping out during their first academic year, using historical student data.

---

## Dataset Description

- **Total records:** 550
- **Total variables:** 11 (10 input features + 1 target variable)
- **Target variable:** `dropout` (Yes / No)

### Variables

| Variable | Type | Description | Range / Values |
|---|---|---|---|
| `age` | Numeric | Student age at enrollment | 16–29 |
| `gender` | Categorical | Student gender | Male, Female, Other |
| `city origin` | Categorical | City where the student comes from | Barranquilla, Bogotá, Medellín, Cali, Other |
| `hs gpa` | Numeric | High school grade point average | 2.5–5.0 |
| `admission score` | Numeric | Admission test score | 200–500 |
| `first sem gpa` | Numeric | First semester GPA at university | 1.5–5.0 |
| `socioeconomic level` | Numeric | Socioeconomic stratum | 1–6 |
| `scholarship` | Categorical | Whether the student has a scholarship | Yes, No |
| `loan` | Categorical | Whether the student has a student loan | Yes, No |
| `financial aid` | Categorical | Whether the student receives financial aid | Yes, No |
| `dropout` | Categorical (Target) | Whether the student dropped out | Yes, No |

---

## Dropout Logic

The target variable was not assigned randomly. It was generated using a weighted probability model that reflects realistic dropout risk factors:

| Factor | Weight |
|---|---|
| First semester GPA < 3.0 | 40% |
| Socioeconomic level ≤ 2 | 20% |
| No scholarship | 15% |
| High school GPA < 3.5 | 10% |
| Admission score < 300 | 10% |
| No student loan | 5% |

Final dropout probabilities were normalized and clipped between 0.05 and 0.95 to avoid extreme determinism.

---

## Null Values

Null values were introduced randomly to simulate real-world data quality issues. Approximately **5% of values** were set to `NaN` in the following numeric columns:

| Column | Null Count (approx.) |
|---|---|
| `age` | ~27 |
| `hs gpa` | ~25 |
| `admission score` | ~27 |
| `first sem gpa` | ~26 |
| `socioeconomic level` | ~27 |

Categorical columns (`gender`, `city origin`, `scholarship`, `loan`, `financial aid`, `dropout`) contain no null values.

---

## Outliers

A total of **15 records** were manually modified to introduce outlier values, simulating data entry errors or extreme cases:

| Column | Outlier Values Introduced |
|---|---|
| `age` | 5, 65, 70 |
| `hs gpa` | 0.5, 5.8, 6.2 |
| `first sem gpa` | 0.2, 5.9, 6.5 |

These outliers fall outside the expected valid ranges and should be handled during the data preprocessing phase.

---

## How to Generate the Dataset

The dataset was generated using Python with the following libraries:
```bash
pip install pandas numpy
```

Run the script:
```bash
python generate dataset.py
```

This will produce `student dropout dataset.csv` with 550 records in the current directory.

---

## Recommended ML Approach

Given that:
- The data is labeled (we know which students dropped out)
- The target variable is binary (Yes / No)

The recommended approach is **Supervised Learning — Classification**.

The selected model is **Random Forest**, chosen for its:
- Robustness against null values and outliers
- Ability to handle mixed variable types (numeric and categorical)
- High accuracy in binary classification
- Feature importance output (identifies which variables influence dropout most)

---

## Author

[Jorge Estiven Burgos Ortega]

**Course:** Data Mining
**Institution:** Universidad de la Costa
**Professor:** José Escorcia-Gutierrez, Ph.D.
