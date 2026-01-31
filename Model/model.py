import pandas as pd
import numpy as np

df = pd.read_csv('X500_Drone_Navigation_PathPlanning_FINALData_2000.csv')

def calculate_risk(row):
    payload_factor = row['Payload_Kg'] / 2.0
    duration_factor = row['Duration_Min'] / 5.0
    distance_factor = row['Distance_Km'] / 3.0
    
    risk_score = (payload_factor * 0.2) + (duration_factor * 0.5) - (distance_factor * 0.3)
    return np.clip(np.round(risk_score, 2), 0, 1)

df['Risk_Score'] = df.apply(calculate_risk, axis=1)

df['Action'] = df['Risk_Score'].apply(
    lambda x: 'INSPECT_DRONE' if x > 0.80 else ('MONITOR_GCS' if x > 0.60 else 'PROCEED')
)

report_filename = "ModelDataAnalysis_X500_Drone_Navigation_PathPlanning_FINALData_2000.txt"

with open(report_filename, "w") as f:
    f.write("=== PREDICTIVE RISK MODEL REPORT ===\n")
    f.write(f"Timestamp: {pd.Timestamp.now()}\n")
    f.write("-----------------------------------------------\n\n")

    inspections = len(df[df['Action'] == 'INSPECT_DRONE'])
    f.write(f"[PREDICTION: MAINTENANCE]\n")
    f.write(f"Based on current model, {inspections} drones requires any inspection/repairment. \n")

    f.write(f"[PREDICTION: LABOR COACHING]\n")
    operator_audit = df.groupby('Operator_ID')['Risk_Score'].mean().sort_values(ascending=False)
    top_risk_op = operator_audit.index[0]
    f.write(f"The model identifies {top_risk_op} as the primary performance bottleneck.\n")

    f.write(f"[PREDICTION: OPERATIONAL BENCHMARKS]\n")
    avg_risk = df['Risk_Score'].mean()
    f.write(f"Current Site-Wide Risk Index: {avg_risk:.2f}\n")
    if avg_risk > 0.5:
        f.write("ALERT: Fleet efficiency is below benchmark. Suggest route optimization.\n")
    else:
        f.write("STATUS: Fleet is operating within optimal Lean parameters.\n\n")

    f.write("--- FULL OPERATOR RISK SUMMARY ---\n")
    f.write(operator_audit.to_string())

print(f"Report Generated: {report_filename}")
