import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('X500_Drone_Navigation_PathPlanning_FINALData_2000.csv')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Payload_Kg', y='Duration_Min', hue='Status', alpha=0.6)
plt.title('Impact of Payload on Flight Duration and Status')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('PayloadAnalysis_X500_Drone_Navigation_PathPlanning_FINALData_2000.png')

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Status', y='Payload_Kg', palette='Set2')
plt.title('Payload Distribution Across Mission Statuses')
plt.savefig('DefectDistribution_X500_Drone_Navigation_PathPlanning_FINALData_2000.png')

print("\nCharts generated: payload_analysis.png and defect_distribution.png")
