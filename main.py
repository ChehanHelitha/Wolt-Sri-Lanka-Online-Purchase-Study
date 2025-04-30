import pandas as pd

excel_file_path = 'In22-CS3121-Project Dataset.xlsx'

try:
    df = pd.read_excel(excel_file_path)
    print("Excel file loaded successfully into DataFrame:")
except FileNotFoundError:
    print(f"Error: The file {excel_file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# --- Initial Inspection ---
print("\nFirst 5 rows of the data:")
print(df.head())

print("\nDataFrame Info (columns, data types, non-null counts):")
df.info()

print("\nBasic Descriptive Statistics for numerical columns:")
print(df.describe())

print(f"\nShape of the DataFrame (rows, columns): {df.shape}")


print(df)
