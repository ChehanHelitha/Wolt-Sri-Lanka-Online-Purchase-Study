import pandas as pd
import numpy as np
import os

excel_file_path = 'In22-CS3121-Project Dataset.xlsx'
excel_output_path = 'cleaned_data.xlsx'


# --- Data Cleaning and Preprocessing ---

# --- Gender Column(B) ---
# Male-553, Female-279, Prefer not to say-4, No Null values, Therfore no need to handle missing values
# Convert to lowercase, strip whitespace, and encode
def preprocess_gender(df, column_name):
    """
    Cleans and encodes the Gender column.
    - Converts to lowercase, strips whitespace.
    - Maps Male -> 1, Female -> 2, Prefer not to say -> 0.
    - Encodes original NaN and any unmapped values to NA_ENCODING_VALUE.
    """
    encoded_col_name = column_name + '_encoded'
    print(f"\n--- Preprocessing Column: '{column_name}' ---")

    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in DataFrame.")
        return df

    print("Original unique values:", df[column_name].unique())

    # Create a copy to avoid modifying original during cleaning steps
    cleaned_series = df[column_name].copy()

    # 1. Standardize: strip whitespace
    cleaned_series = cleaned_series.astype(str).str.lower().str.strip()

    print("Unique values after standardization:", cleaned_series.unique())

    # 2. Define mapping
    gender_map = {
        'male': 1,
        'female': 2,
        'prefer not to say': 0
    }

    # 3. Apply mapping
    df[encoded_col_name] = cleaned_series.map(gender_map)

    # Convert to integer type as it now only contains numbers
    df[encoded_col_name] = df[encoded_col_name].astype(int)

    print(f"Mapped 'male'->1, 'female'->2, 'prefer not to say'->0.")
    print(f"Created encoded column: '{encoded_col_name}'")
    print("Unique values in encoded column:", df[encoded_col_name].unique())

    return df


# --- Function to clean and encode Yes/No columns ---
# The column 'Have used online shopping platforms before'(F) has 833-"Yes", 3-"No" and no null values.
# The column 'Have you made online purchases during crisis time?'(BC) has 809-"Yes", 27-"No" and no null values.
# Therefore no need to handle missing values.
# Convert to lowercase, strip whitespace, and encode
def preprocess_yes_no(df, column_name):
    """
    Cleans and encodes a Yes/No column.
    - Converts to lowercase, strips whitespace.
    - Maps Yes -> 1, No -> 0.
    """
    encoded_col_name = column_name + '_encoded'
    print(f"\n--- Preprocessing Column: '{column_name}' ---")

    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in DataFrame.")
        return df

    print("Original unique values:", df[column_name].unique())

    # Create a copy to avoid modifying original during cleaning steps
    cleaned_series = df[column_name].copy()

    # 1. Standardize: Lowercase and strip whitespace (handle potential float NaNs)
    cleaned_series = cleaned_series.astype(str).str.lower().str.strip()

    print("Unique values after standardization", cleaned_series.unique())

    # 2. Define mapping
    yes_no_map = {
        'yes': 1,
        'no': 0
    }

    # 3. Apply mapping
    df[encoded_col_name] = cleaned_series.map(yes_no_map)

    # Convert to integer type
    df[encoded_col_name] = df[encoded_col_name].astype(int)

    print(f"Mapped 'yes'->1, 'no'->0.")
    print(f"Created encoded column: '{encoded_col_name}'")
    print("Unique values in encoded column:", df[encoded_col_name].unique())

    return df

try:
    df = pd.read_excel(excel_file_path)
    print("Excel file loaded successfully into DataFrame:")

    # --- Initial Inspection ---
    # print("\nFirst 5 rows of the data:")
    # print(df.head())
    # print("\nDataFrame Info (columns, data types, non-null counts):")
    # df.info()
    # print("\nBasic Descriptive Statistics for numerical columns:")
    # print(df.describe())
    # print(f"\nShape of the DataFrame (rows, columns): {df.shape}")

    # --- Data Cleaning and Preprocessing ---
    # 1. Define column names
    gender_col = 'Gender'
    used_platforms_col = 'Have used online shopping platforms before '
    purchased_crisis_col = 'Have you made online purchases during crisis time?'

    # 2. Apply preprocessing functions
    df = preprocess_gender(df, column_name=gender_col)
    df = preprocess_yes_no(df, column_name=used_platforms_col)
    df = preprocess_yes_no(df, column_name=purchased_crisis_col)

    # 3. Save the cleaned data to a new Excel file
    print(f"\nSaving cleaned data to: {excel_output_path}")
    # Use engine='openpyxl' for .xlsx format
    df.to_excel(excel_output_path, index=False, engine='openpyxl')
    print("Cleaned data saved successfully.")

except FileNotFoundError:
    print(f"Error: The file {excel_file_path} was not found.")
except KeyError as e:
    print(f"Error: Column {e} not found. Please check the column names in your Excel file.")
    print("Current DataFrame columns:", df.columns.tolist())
except Exception as e:
    print(f"An unexpected error occurred: {e}")