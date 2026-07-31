import os

import pandas as pd


# Find the project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "use_case.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the CSV file
use_case_data = pd.read_csv(data_file)

# Read the first row
first_row = use_case_data.iloc[0]

business_problem = first_row["BusinessProblem"]
current_method = first_row["CurrentMethod"]
ai_objective = first_row["AIObjective"]
expected_benefit = first_row["ExpectedBenefit"]

# Create report file
report_file = os.path.join(output_folder, "ai_usecase_report.txt")

with open(report_file, "w", encoding="utf-8") as report:

    report.write("AI USE CASE DESIGN\n")
    report.write("=" * 40 + "\n\n")

    report.write("Business Problem\n")
    report.write("----------------\n")
    report.write(business_problem)
    report.write("\n\n")

    report.write("Current Method\n")
    report.write("--------------\n")
    report.write(current_method)
    report.write("\n\n")

    report.write("AI Objective\n")
    report.write("------------\n")
    report.write(ai_objective)
    report.write("\n\n")

    report.write("Expected Benefit\n")
    report.write("----------------\n")
    report.write(expected_benefit)
    report.write("\n\n")

    report.write("Conclusion\n")
    report.write("----------\n")
    report.write(
        "Artificial Intelligence can reduce manual work, "
        "improve efficiency, and support better business decisions."
    )

print("AI use case report created successfully.")
print("Report saved in:", report_file)