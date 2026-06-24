# Data Dictionary

## 07_scheme_performance.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | AMFI Scheme Code |
| scheme_name | Text | Mutual Fund Scheme Name |
| fund_house | Text | Fund House Name |
| category | Text | Fund Category |
| return_1yr_pct | Float | 1 Year Return (%) |
| return_3yr_pct | Float | 3 Year Return (%) |
| return_5yr_pct | Float | 5 Year Return (%) |
| expense_ratio_pct | Float | Expense Ratio (%) |
| aum_crore | Float | Assets Under Management |
| risk_grade | Text | Risk Classification |

## 02_nav_history_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | AMFI Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

## 08_investor_transactions_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor Identifier |
| transaction_date | Date | Transaction Date |
| amfi_code | Integer | AMFI Scheme Code |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| city_tier | Text | Tier Classification |
| age_group | Text | Investor Age Group |
| gender | Text | Investor Gender |
| annual_income_lakh | Float | Annual Income (Lakhs) |
| payment_mode | Text | Payment Method |
| kyc_status | Text | KYC Verification Status |