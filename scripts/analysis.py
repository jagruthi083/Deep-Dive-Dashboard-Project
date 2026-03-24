import pandas as pd

df = pd.read_csv('../data/data.csv')

# KPIs
conversion_rate = len(df[df['orders'] > 1]) / len(df) * 100
churn_rate = df['churned'].mean() * 100
aov = df['revenue'].sum() / df['orders'].sum()

print(f"Conversion Rate: {conversion_rate:.2f}%")
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Average Order Value: {aov:.2f}")

# Cohort Analysis
df['signup_month'] = pd.to_datetime(df['signup_date']).dt.to_period('M')

cohort = df.groupby('signup_month').agg({
    'customer_id': 'count',
    'revenue': 'sum'
})

print("\nCohort Analysis:\n", cohort.head())
