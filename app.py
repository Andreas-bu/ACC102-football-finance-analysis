import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Football Finance Analysis", layout="wide")

st.title("🏟️ Top 20 Football Clubs Financial Health Analysis")
st.subheader("2020–2024 | ACC102 Track 2 Data Product")

# Load data
@st.cache_data
def load_data():
    financial = pd.read_csv("financial_data.csv", encoding="utf-8-sig")
    performance = pd.read_csv("performance_data.csv", encoding="utf-8-sig")
    return financial, performance

financial_df, performance_df = load_data()

# Data transformation
df = financial_df.copy()
df = df.rename(columns={
    'Club Name': 'Club',
    'Total Revenue (€m)': 'Total_Revenue',
    'Commercial Revenue (€m)': 'Commercial_Revenue',
    'Wages/Revenue Ratio (%)': 'Wages_Ratio'
})

df['Total_Revenue'] = pd.to_numeric(df['Total_Revenue'], errors='coerce')
df['Commercial_Revenue'] = pd.to_numeric(df['Commercial_Revenue'], errors='coerce')
df['Wages_Ratio'] = pd.to_numeric(df['Wages_Ratio'], errors='coerce')

df['Wages_Amount'] = df['Total_Revenue'] * (df['Wages_Ratio'] / 100)
df['Commercial_Share'] = (df['Commercial_Revenue'] / df['Total_Revenue']) * 100

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_clubs = st.sidebar.multiselect(
    "Select Clubs",
    options=df['Club'].unique(),
    default=["Real Madrid", "Manchester City"]
)

selected_years = st.sidebar.multiselect(
    "Select Years",
    options=sorted(df['Year'].unique()),
    default=[2024]
)

# Filter data
filtered_df = df[(df['Club'].isin(selected_clubs)) & (df['Year'].isin(selected_years))]

# Main content
st.subheader("📋 Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# Chart 1: Wages/Revenue Ratio with FFP threshold
st.subheader("1. Wages/Revenue Ratio (2024) - UEFA FFP 70% Warning")
if not filtered_df.empty and 2024 in filtered_df['Year'].values:
    df_2024 = filtered_df[filtered_df['Year'] == 2024]
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_2024.sort_values('Wages_Ratio', ascending=False),
                x='Club', y='Wages_Ratio', ax=ax1, palette="Blues_d")
    ax1.axhline(y=70, color='red', linestyle='--', linewidth=2.5, label='UEFA FFP 70% Threshold')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
    ax1.set_ylabel("Wages/Revenue Ratio (%)")
    ax1.legend()
    st.pyplot(fig1)

# Chart 2: Commercial Revenue Share
st.subheader("2. Commercial Revenue Share (%)")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_df.sort_values('Commercial_Share', ascending=False),
            x='Club', y='Commercial_Share', ax=ax2, palette="Greens_d")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
ax2.set_ylabel("Commercial Revenue Share (%)")
st.pyplot(fig2)

# Chart 3: 5-year trend for selected clubs
st.subheader("3. 5-Year Wages Ratio Trend")
trend_df = df[df['Club'].isin(selected_clubs)]
if not trend_df.empty:
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=trend_df, x='Year', y='Wages_Ratio', hue='Club', 
                 marker='o', linewidth=2.5, ax=ax3)
    ax3.set_ylabel("Wages/Revenue Ratio (%)")
    ax3.grid(True)
    st.pyplot(fig3)

# Accounting insights
st.subheader("💼 Key Accounting Insights")
st.write("""
- Clubs with higher revenue tend to have better cost discipline (lower wages ratio).
- Commercial revenue share is a strong indicator of financial resilience.
- Several clubs exceeded the UEFA FFP 70% warning threshold in 2024.
- European success shows a lagged positive effect on commercial revenue growth.
""")

st.caption("Data source: Deloitte Football Money League 2025 Report | Accessed: April 2026")
