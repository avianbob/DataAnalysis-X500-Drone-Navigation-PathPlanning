import pandas as pd
import sqlite3

input_filename = 'X500_Drone_Navigation_PathPlanning_FINALData_2000.csv' 
output_filename = 'SQLDataAnalysisX500_Drone_Navigation_PathPlanning_FINALData_2000.txt'

try:
    df = pd.read_csv(input_filename)

    conn = sqlite3.connect(':memory:')
    df.to_sql('flights', conn, index=False)

    with open(output_filename, 'w') as f:
        
        query_a = """
        SELECT 
            Operator_ID,
            COUNT(*) AS Total_Flights,
            SUM(CASE WHEN Status != 'Success' THEN 1 ELSE 0 END) AS Total_Defects,
            ROUND(SUM(CASE WHEN Status != 'Success' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Defect_Percentage
        FROM flights
        GROUP BY Operator_ID
        ORDER BY Defect_Percentage DESC;
        """
        
        df_result_a = pd.read_sql_query(query_a, conn)
        
        f.write("--- PATH PLANNING PERFORMANCE (DEFECT RATE) ---\n")
        f.write(df_result_a.to_string(index=False))
        f.write("\n\n")

        query_b = """
        SELECT 
            Status,
            COUNT(*) as Occurrence,
            ROUND(AVG(Payload_Kg), 2) as Avg_Payload
        FROM flights
        GROUP BY Status;
        """
        
        df_result_b = pd.read_sql_query(query_b, conn)
        
        f.write("--- SYSTEM BOTTLENECKS ---\n")
        f.write(df_result_b.to_string(index=False))
        f.write("\n")

    conn.close()
    print(f"Success! Queries executed and saved to '{output_filename}'")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except pd.errors.DatabaseError as e:
    print(f"Database Error: {e}")
