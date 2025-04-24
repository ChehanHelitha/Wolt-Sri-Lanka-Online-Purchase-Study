import pandas as pd
import pingouin as pg

excel_file_path = 'In22-CS3121-Project Dataset.xlsx'

try:
    df = pd.read_excel(excel_file_path)
    print("Excel file loaded successfully into DataFrame:")
except FileNotFoundError:
    print(f"Error: The file {excel_file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

"""
# --- Initial Inspection ---
print("\nFirst 5 rows of the data:")
print(df.head())

print("\nDataFrame Info (columns, data types, non-null counts):")
df.info()

print("\nBasic Descriptive Statistics for numerical columns:")
print(df.describe())

print(f"\nShape of the DataFrame (rows, columns): {df.shape}")
"""

import pingouin as pg

# Define question lists based on Table 1 (adjust column names as needed)
# Assuming column names are 'Q13', 'Q14', ... 'Q52'
peou_cols = [f'Q{i}' for i in range(13, 23)] # Q13 to Q22
pu_cols = [f'Q{i}' for i in range(23, 33)]  # Q23 to Q32
sa_cols = [f'Q{i}' for i in range(33, 39)]  # Q33 to Q38
si_cols = [f'Q{i}' for i in range(39, 51)]  # Q39 to Q50
intention_cols = [f'Q{i}' for i in range(51, 53)] # Q51, Q52

# Ensure all columns exist in the DataFrame before proceeding
all_survey_cols = peou_cols + pu_cols + sa_cols + si_cols + intention_cols
missing_cols = [col for col in all_survey_cols if col not in df.columns]
if missing_cols:
    print(f"Error: The following expected columns are missing: {missing_cols}")
    # Handle error appropriately
    exit()

# --- Calculate Cronbach's Alpha ---
print("\n--- Cronbach's Alpha ---")

# Drop rows with NaN in the specific subset before calculating alpha
alpha_peou = pg.cronbach_alpha(data=df[peou_cols].dropna())
print(f"PEOU ({len(peou_cols)} items): Alpha = {alpha_peou[0]:.3f}")

alpha_pu = pg.cronbach_alpha(data=df[pu_cols].dropna())
print(f"PU ({len(pu_cols)} items): Alpha = {alpha_pu[0]:.3f}")

alpha_sa = pg.cronbach_alpha(data=df[sa_cols].dropna())
print(f"SA ({len(sa_cols)} items): Alpha = {alpha_sa[0]:.3f}")

alpha_si = pg.cronbach_alpha(data=df[si_cols].dropna())
print(f"SI ({len(si_cols)} items): Alpha = {alpha_si[0]:.3f}")

# Alpha for 2 items is equivalent to correlation, but pg.cronbach_alpha handles it
alpha_intention = pg.cronbach_alpha(data=df[intention_cols].dropna())
print(f"Intention ({len(intention_cols)} items): Alpha = {alpha_intention[0]:.3f}")