# DataAnalysis-X500-Drone-Navigation-PathPlanning

This project simulates the operational lifecycle of a 2000 mission autonomous drone fleet (X500).

The goal was to benchmark fleet reliability, identify human-induced performance bottlenecks, and develop a predictive risk model.
---

## Data Acquisition
* **Environment:** PX4 Autopilot integrated with Depth Camera SLAM for autonomous navigation.
* **Methodology:** Ran headless simulations at 10x real-time speed via CLI.
* **Scale:** Simulated 300 hours of continuous operations in just 30 hours of compute time.
* **Integrity:** Captured 2,000 sequential flights including timestamps, distance, duration, and mission status.

---

## Project Structure & Workflow
### /Data
It contains the raw logs from the PX4 simulation and the processed versions. I included a script here to assign flights to 10 different "Operator IDs." I did this to simulate a multi-user environment and see if mission failures were tied to specific handling styles or turnaround gaps.

### /Excel
This folder contains the initial data deep-dive. Using Pivot Tables, I analyzed success/failure ratios and payload distributions. It provides a quick way to see which operator IDs were most efficient and how different weights (from 0.5kg to 2.0kg) impacted the fleet.

### /SQL
For more granular analysis, I used SQL to query the dataset. This allowed for complex filtering of hardware disconnects (GCS Disconnects) and helped identify systemic issues that aren't easily visible in a spreadsheet.


### /Graphs
The visualization layer. Using **Seaborn** and **Matplotlib**, I generated scatter plots and box plots to find correlations between payload weight, flight duration, and mission success. 


### /Model
The final stage of the pipeline. I built a predictive script that calculates an **Efficiency Ratio** based on Distance vs. Duration. The model flags missions as "Optimal," "Monitor," or "Investigate," creating a roadmap for improving future flight paths.
---

## How to Run the Analysis
1. **Prepare Data:** Run `python3 Data/divide_operator.py` to generate the final operator-assigned dataset.
2. **Execute SQL Audit:** Run `python3 SQL/analysis.py` for site-wide defect reporting.
3. **Generate Visuals:** Run `python3 Graphs/generate_graphs.py` to create charts.
4. **Predictive Modeling:** Run `python3 Model/model.py` to view actionable risk assessments.

---
