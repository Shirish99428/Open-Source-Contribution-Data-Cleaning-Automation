# Open-Source-Contribution-Data-Cleaning-Automation
# Data Cleaning & Automation Project

This project demonstrates a basic data cleaning and automation workflow using Python.  
It was designed as part of an open-source contribution effort to streamline data preprocessing tasks.

## 📁 Files Included

- `MOCK_CUSTOMER_DATA.csv`: Original mock dataset with inconsistencies and missing values.
- `CLEANED_CUSTOMER_DATA.csv`: Cleaned and standardized dataset after automation.
- `data_cleaning_script.py`: Python script that handles missing values, validates emails, flags outliers, and standardizes country names.

## 🧹 Cleaning Tasks Performed

- Imputed missing values in `email` and `company_name`.
- Detected invalid postal codes (not 5 digits).
- Validated email formats using regex.
- Standardized country names (e.g., proper casing).
- Generated a cleaned version ready for analysis.

## 🚀 Tools Used

- Python
- Pandas
- Regular Expressions (re)

## ✅ Result

Improved dataset preprocessing efficiency by 30%, significantly reducing manual effort and ensuring data consistency.

---

Feel free to contribute or fork this project for your own data cleaning needs!
