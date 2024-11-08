import pandas as pd

# Paths to CSV files
file1_path = r"C:\Users\HP\Downloads\clang 19 ggml_1 - sgemm.cpp.json.csv"
file2_path = r"C:\Users\HP\Downloads\clang 19 ggml_2 - sgemm.cpp.json.csv"
file3_path = r"C:\Users\HP\Downloads\clang 19 ggml_3 - sgemm.cpp.json.csv"

# Load the CSV files
df1 = pd.read_csv(file1_path, usecols=[0, 1, 2])
df2 = pd.read_csv(file2_path, usecols=[0, 1, 2])
df3 = pd.read_csv(file3_path, usecols=[0, 1, 2])

# Merge the dataframes to find common function names in all three files
merged_df = df1.merge(df2, on="Function_name", suffixes=('_1', '_2')).merge(df3, on="Function_name")

# Calculate the average
merged_df['average_duration'] = merged_df[['Total Duration (μs)_1', 'Total Duration (μs)_2', 'Total Duration (μs)']].mean(axis=1)
merged_df['average_percentage'] = merged_df[['computational percentage (%)_1', 'computational percentage (%)_2', 'computational percentage (%)']].mean(axis=1)

# Select only the relevant columns for output
result_df = merged_df[['Function_name', 'average_duration', 'average_percentage']]

# Save the result to a new CSV file
output_path = 'common_functions_average.csv'
result_df.to_csv(output_path, index=False)

print(f"Output saved to {output_path}")