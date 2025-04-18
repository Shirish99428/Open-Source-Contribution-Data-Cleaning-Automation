
import pandas as pd
import re

# Load dataset
df = pd.read_csv("MOCK_CUSTOMER_DATA.csv")

# Fill missing values
df['email'].fillna('unknown@example.com', inplace=True)
df['company_name'].fillna('Not Provided', inplace=True)

# Validate email format
def is_valid_email(email):
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))

df['email_invalid'] = ~df['email'].apply(is_valid_email)

# Detect outliers in postal_code (not 5 digits)
df['postal_code_invalid'] = ~df['postal_code'].astype(str).str.match(r'^\d{5}$')

# Standardize country names
df['country'] = df['country'].str.strip().str.title()

# Save cleaned dataset
df.to_csv("CLEANED_CUSTOMER_DATA.csv", index=False)
