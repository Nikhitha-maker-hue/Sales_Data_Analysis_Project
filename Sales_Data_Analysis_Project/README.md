# Sales Data Analysis

## Project Overview
This portfolio project analyzes one year of retail sales data to identify:
- Revenue trends over time
- Top-performing products
- Customer segment patterns
- Regional performance
- Sales-channel performance
- Profitability and key business KPIs

## Tools Used
- Python
- Pandas
- Matplotlib
- Excel
- CSV

## Dataset
The project includes a generated sample dataset with 1,800 sales orders from 2025.

Important columns:
- `Order_ID`
- `Order_Date`
- `Customer_ID`
- `Product`
- `Category`
- `Region`
- `City`
- `Customer_Segment`
- `Sales_Channel`
- `Quantity`
- `Unit_Price`
- `Discount`
- `Revenue`
- `Cost`
- `Profit`

## Project Structure

```text
Sales_Data_Analysis_Project/
│
├── data/
│   └── sales_data.csv
│
├── output/
│   ├── Sales_Analysis_Report.xlsx
│   ├── monthly_summary.csv
│   ├── product_summary.csv
│   ├── region_summary.csv
│   ├── segment_summary.csv
│   └── charts/
│
├── src_analysis.py
├── requirements.txt
└── README.md
```

## How to Run

1. Install Python 3.10+.
2. Open a terminal in the project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run:

```bash
python src_analysis.py
```

5. Open `output/Sales_Analysis_Report.xlsx` for the Excel dashboard and detailed analysis.

## Business Questions Answered
1. How much revenue and profit did the business generate?
2. Which months generated the highest revenue?
3. Which products are the top revenue contributors?
4. Which regions generate the most sales?
5. Which customer segments contribute most revenue?
6. Which sales channel performs best?
7. What is the average order value?
8. What is the overall profit margin?

## Portfolio / Resume Description
**Sales Data Analysis | Python, Pandas, Excel**
Analyzed 1,800+ sales transactions to identify revenue trends, top-performing products, customer segment patterns, regional performance and profitability. Used Python/Pandas for data cleaning and aggregation and Excel to build KPI summaries and a management dashboard.
