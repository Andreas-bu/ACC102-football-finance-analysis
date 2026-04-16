# ACC102-football-finance-analysis

## 2020–2024 Top 20 Football Clubs Financial Health Analysis

**ACC102 Track 4: Interactive Data Analysis Tool**  
**Product**: Streamlit Interactive Web App

---

## Problem & User

Do higher revenues automatically lead to better financial health?  

This project examines **cost control** (measured by Wages/Revenue Ratio) and **revenue diversification** (especially commercial revenue) among the world's top 20 revenue-generating football clubs, while linking financial metrics to on-pitch performance.

**Target audience**: Club financial directors, sports investors, and accounting professionals interested in sustainable football club business models and UEFA Financial Fair Play (FFP) compliance.

---

## Data

- **Financial Data**: 20 clubs × 5 years (2020–2024) from Deloitte Football Money League 2025 report  
  Columns: Club Name, Year, Total Revenue (€m), Commercial Revenue (€m), Wages/Revenue Ratio (%)
- **Performance Data**: 5-year league and European competition results for Real Madrid, AC Milan, and Paris Saint-Germain
- Data accessed: 13 April 2026

---

## Methods

- Interactive web application built with **Streamlit** (app.py)
- Supporting analytical workflow in Jupyter Notebook (`football_analysis_csv.ipynb`)
- Data loading, cleaning, and feature engineering (new columns: Wages Amount, Commercial Share %)
- 2024 cross-sectional analysis with interactive filters, bar charts, scatter plots with regression
- 5-year longitudinal case study with dynamic multi-line trends and dual-axis visualizations
- Libraries: pandas, matplotlib, seaborn, streamlit

---

## Key Findings

**2024 Cross-Sectional Analysis (20 clubs)**
- Significant variation in cost control: Real Madrid achieved the lowest Wages/Revenue Ratio (48%) despite being the highest revenue club.
- Clear negative correlation between total revenue and wages ratio (higher revenue clubs tend to have stronger cost discipline).
- Several clubs exceeded the UEFA FFP warning threshold of 70%.

**5-Year Longitudinal Case Study (Real Madrid, AC Milan, PSG)**
- Real Madrid demonstrated strong financial resilience: wages ratio spiked in 2022 during stadium redevelopment but dropped sharply to 48% in 2024 as commercial revenue surged.
- Clubs with higher commercial revenue share showed faster recovery and more stable cost control.
- On-pitch success (e.g. Champions League performance) has a lagged positive impact on revenue diversification.

---

## How to Run

### 🌐 Online Demo (Recommended)

**[Open Interactive Web App](https://andreas-bu-acc102-football-finance-analysis-app-vzrdmo.streamlit.app)**

Use the filters on the left to explore clubs, years, wages ratio range, and commercial share interactively.

### 1. Run Locally with Streamlit (Interactive Tool)

```bash
git clone https://github.com/Andreas-bu/ACC102-football-finance-analysis.git
cd ACC102-football-finance-analysis

pip install -r requirements.txt
streamlit run app.py

jupyter notebook football_analysis_csv.ipynb
