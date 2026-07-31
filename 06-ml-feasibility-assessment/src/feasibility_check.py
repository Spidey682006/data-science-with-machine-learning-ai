import os

import pandas as pd


project_folder = os.path.dirname(os.path.dirname(__file__))

data_file = os.path.join(project_folder, "data", "customer_churn.csv")
output_folder = os.path.join(project_folder, "outputs")

os.makedirs(output_folder, exist_ok=True)

dataset = pd.read_csv(data_file)

total_rows = len(dataset)
total_columns = len(dataset.columns)

missing_values = dataset.isnull().sum().sum()

target_column = "churn"

recommendation = "Not Determined"
reason = ""

if target_column in dataset.columns:

    unique_values = dataset[target_column].unique()

    if len(unique_values) <= 10:
        recommendation = "Classification"
        reason = (
            "The target column contains categories "
            "such as Yes and No."
        )

    else:
        recommendation = "Regression"
        reason = (
            "The target column contains many "
            "numerical values."
        )

else:

    recommendation = "Clustering"
    reason = (
        "No target column was found, so "
        "unsupervised learning is recommended."
    )

report_file = os.path.join(
    output_folder,
    "ml_feasibility_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("MACHINE LEARNING FEASIBILITY REPORT\n")
    report.write("=" * 45 + "\n\n")

    report.write(f"Dataset Records : {total_rows}\n")
    report.write(f"Dataset Columns : {total_columns}\n")
    report.write(f"Missing Values : {missing_values}\n\n")

    report.write(f"Target Column : {target_column}\n")
    report.write(f"Recommended Approach : {recommendation}\n\n")

    report.write("Reason\n")
    report.write("-" * 20 + "\n")
    report.write(reason + "\n\n")

    report.write("Conclusion\n")
    report.write("-" * 20 + "\n")

    report.write(
        "The dataset is suitable for Machine Learning.\n"
    )

    report.write(
        f"The recommended approach is {recommendation}."
    )

print("Feasibility assessment completed.")
print("Report saved in:", report_file)