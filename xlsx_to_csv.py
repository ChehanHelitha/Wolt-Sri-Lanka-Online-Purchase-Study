import pandas as pd
import os 


excel_file_path = 'In22-CS3121-Project Dataset.xlsx' 
csv_file_path = 'data.csv'

try:
    print(f"Reading Excel file: {excel_file_path}...")
    df = pd.read_excel(excel_file_path, engine='openpyxl')

    print(f"Writing DataFrame to CSV file: {csv_file_path}...")

    # index=False prevents pandas from writing the DataFrame index as a column
    # encoding='utf-8' is generally a good choice for compatibility
    df.to_csv(csv_file_path, index=False, encoding='utf-8')

    print("-" * 30)
    print(f"Successfully converted '{os.path.basename(excel_file_path)}' to '{os.path.basename(csv_file_path)}'")
    print("-" * 30)

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found.")
    print("Please check the file path and name.")

except Exception as e:
    print(f"An error occurred during conversion: {e}")