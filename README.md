# Student Dropout Dataset

Synthetic dataset simulating undergraduate student dropout prediction.

## Variables
| Variable | Type | Range / Values |
|---|---|---|
| age | Numeric | 16–30 (outliers: 5, 65, 70) |
| gender | Categorical | Male, Female, Other |
| city_origin | Categorical | Barranquilla, Bogotá, Medellín, Cali, Other |
| hs_gpa | Numeric | 2.5–5.0 |
| admission_score | Numeric | 200–500 |
| first_sem_gpa | Numeric | 1.5–5.0 |
| socioeconomic_level | Numeric | 1–6 |
| scholarship | Categorical | Yes, No |
| loan | Categorical | Yes, No |
| financial_aid | Categorical | Yes, No |
| dropout | Target | Yes, No |

## Nulls
~5% null values introduced randomly in: age, hs_gpa, admission_score, 
first_sem_gpa, socioeconomic_level.

## Outliers
15 records with extreme values introduced in: age (5, 65, 70), 
hs_gpa (0.5, 5.8, 6.2), first_sem_gpa (0.2, 5.9, 6.5).
