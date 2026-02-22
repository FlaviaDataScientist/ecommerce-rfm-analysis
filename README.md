# LIVE ON: https://ecommerce-rfm-analysis-ivxsafbqjqbyiyqxnjfxek.streamlit.app/

# ecommerce-rfm-analysis
International (EN/DE) Customer Segmentation Dashboard using Python, Pandas, and Streamlit.

# 📊 International E-Commerce RFM Analysis

This project provides an end-to-end data science solution for customer segmentation. 
It features a **Bilingual Dashboard (English/German)** built with Streamlit.

## 🌟 Features
- **Data Cleaning:** Handles international CSV formats and currency symbols.
- **RFM Logic:** Scores customers based on Recency, Frequency, and Monetary value.
- **Interactive UI:** Users can filter segments (e.g., Champions, At Risk) in real-time.
- **Dual Language:** Toggle between English and German with one click.

## 🛠️ Technology Stack
- **Python** (Pandas, Plotly)
- **Streamlit** (Web Interface)
- **RFM Modeling** (Marketing Analytics)

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ecommerce-rfm-analysis.git](https://github.com/YOUR_USERNAME/ecommerce-rfm-analysis.git)

📊 International E-Commerce Customer Segmentation (RFM)

This project provides an end-to-end Data Science solution to segment over 4,000 customers for an e-commerce platform. It transforms raw transactional data into actionable marketing insights through a custom-built, bilingual (English/German) interactive dashboard.

📌 Project OverviewThe goal of this project was to automate the process of identifying high-value customers and those at risk of churning. By moving beyond static spreadsheets, I created a dynamic tool that allows stakeholders to filter and export customer lists based on behavioral data.

🚀 Key Milestones & Technical Challenges

Data Engineering & Global Compatibility
The Challenge: 
Transactions often arrive in different European formats, utilizing ; as delimiters and , for decimals, which causes errors in standard Python pipelines.

The Solution: 

I built a robust cleaning pipeline using pandas to standardize date-time objects and numerical values, ensuring the model can process data from various international markets without manual intervention.

RFM Model Implementation To categorize customers, I implemented the RFM Framework:
   Recency: Calculated the number of days since the customer's last purchase.
   Frequency: Quantified the total number of successful transactions.
   Monetary: Aggregated the total lifetime spend per customer.

The Logic: 
Applied quintile-based scoring ($1$–$5$) to create 10 distinct behavioral segments, such as Champions, At Risk, and Loyal Customers.


Analytics Dashboard (Streamlit)
I converted the static Python analysis into a live, professional web application

Real-time Filtering: 
Stakeholders can drill down into specific segments to see their contribution to total revenue.

KPI Tracking: 
Integrated high-level metrics for Total Revenue, Average Spend, and Customer Count.

User Interface: 
Designed for speed and clarity using Streamlit and Plotly.

The Language Feature: 
Built a custom translation engine within the Python script.

The Result: 
A sidebar toggle that switches the entire UI between English and German instantly. This ensures the tool is ready for use by international teams and local German stakeholders.

🛠️ Tech StackLanguage: 
PythonData Analysis: Pandas, NumPy
Visualization: Plotly Express (Interactive Charts)
Web Framework: Streamlit
Environment: Jupyter Notebooks & VS Code

📈 Business Impact Efficiency: 
Automated a segmentation process that previously took hours of manual work in Excel.

Targeting: 
Enabled the marketing team to export specific lists (e.g., "At Risk" customers) for targeted re-engagement email campaigns.

Strategic Insight: 
Provided a clear visual breakdown showing that the top 20% of customers drive the majority of the company's revenue.

