import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Deep Dive Business Dashboard")

df = pd.read_csv('../data/data.csv')

# KPIs
conversion_rate = len(df[df['orders'] > 1]) / len(df) * 100
churn_rate = df['churned'].mean() * 100
aov = df['revenue'].sum() / df['orders'].sum()

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Conversion Rate", f"{conversion_rate:.2f}%")
col2.metric("Churn Rate", f"{churn_rate:.2f}%")
col3.metric("AOV", f"{aov:.2f}")

# Revenue Trend
fig = px.line(df, x='signup_date', y='revenue', title='Revenue Trend')
st.plotly_chart(fig)

# Cohort Analysis
df['signup_month'] = pd.to_datetime(df['signup_date']).dt.to_period('M').astype(str)
cohort = df.groupby('signup_month')['revenue'].sum().reset_index()

fig2 = px.bar(cohort, x='signup_month', y='revenue', title='Cohort Revenue')
st.plotly_chart(fig2)
