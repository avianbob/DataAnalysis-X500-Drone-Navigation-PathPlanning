import pandas as pd
import numpy as np

input_filename = 'X500_Drone_Navigation_PathPlanning_RAWData_2000.csv'
output_filename = 'X500_Drone_Navigation_PathPlanning_FINALData_2000.csv'
num_operators = 10


np.random.seed(42)

try:
    print(f"Reading file: {input_filename}...")
    df = pd.read_csv(input_filename)

    operator_list = [f"OP-{i:03d}" for i in range(1, num_operators + 1)]

    df['Operator_ID'] = np.random.choice(operator_list, size=len(df))

    other_cols = [c for c in df.columns if c not in ['Flight_ID', 'Operator_ID']]
    new_column_order = ['Flight_ID', 'Operator_ID'] + other_cols
    df = df[new_column_order]

    df.to_csv(output_filename, index=False)
    
    print(f"Success! New file created: {output_filename}")
    
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")

