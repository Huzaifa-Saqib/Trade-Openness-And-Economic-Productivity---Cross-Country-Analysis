# Trade Openness & Economic Productivity — Cross-Country Analysis
## Overview
This project investigates the relationship between **trade openness and economic productivity** across **125 countries** using cross-sectional data from the World Bank's World Development Indicators (WDI) for the year 2022. The study analyzes how trade openness, FDI inflows, electricity consumption, and mobile subscriptions influence **GDP per capita**. Insights were visualized through multiple charts and actionable policy recommendations were provided.

---

## Objectives
- Analyze the relationship between trade openness and GDP per capita across 125 countries
- Examine the role of FDI, electricity consumption, and mobile subscriptions as drivers of economic productivity
- Visualize global income inequality and trade patterns
- Provide data-driven recommendations for policymakers and businesses in emerging markets

---

## Data
- **Source:** World Bank World Development Indicators (WDI)
- **Year:** 2022
- **Sample:** 125 countries (after cleaning and outlier removal)
- **Variables:**
  - GDP per capita (constant USD) — Dependent Variable
  - Trade % GDP (Exports + Imports as % of GDP)
  - FDI Inflows (% GDP)
  - Electricity Consumption (kWh per capita)
  - Mobile Subscriptions (per 100 people)

---

## Analysis & Approach
1. Collected data from WDI for all variables across 200+ countries
2. Cleaned and merged datasets using **Python (Pandas)**
3. Applied **log transformation** to GDP per capita to address right skewness
4. Produced 6 visualizations including scatterplots, bar charts and histograms
5. Analyzed relationships using fitted regression lines and R² values
6. Provided actionable business and policy recommendations

---

## Key Findings
- **Electricity consumption** is the strongest predictor of GDP per capita (R² = 0.576), highlighting the critical role of energy infrastructure
- **Mobile subscriptions** show a moderate positive relationship with GDP (R² = 0.22), reflecting the importance of digital connectivity
- **Trade openness** shows a positive relationship with GDP (R² = 0.1589) — high trade countries average $23,000 GDP vs $10,000 for low trade countries
- **FDI** shows a limited direct relationship with GDP (R² = 0.001), suggesting effectiveness depends on institutional quality
- Global income inequality is stark — Norway ($109,269) vs Mozambique ($578), a gap of nearly 200x

---

## Recommendations
- **Infrastructure First:** Governments should prioritize electricity and digital infrastructure before aggressive trade liberalization
- **Trade Policy:** Low trade countries should gradually open trade while building institutional capacity
- **FDI Strategy:** Channel foreign investment into productive sectors rather than purely extractive industries
- **Emerging Markets:** Businesses expanding into new markets should assess infrastructure quality as a key indicator of economic potential

---

## Tools Used
- **Python (Pandas)** for data cleaning and merging
- **Excel** for data analysis and visualization
- **World Bank WDI** as primary data source

```
