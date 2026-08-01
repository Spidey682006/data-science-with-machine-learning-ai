import os

import pandas as pd


# Find the main project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "/workspaces/data-science-with-machine-learning-ai/12-customer-segmentation-profiling/data/customer_segmentation.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the dataset
customer_data = pd.read_csv(data_file)

# Get all cluster numbers
cluster_list = customer_data["Cluster"].unique()
cluster_list = sorted(cluster_list)

# Create lists to store profile information
cluster_numbers = []
customer_counts = []
average_incomes = []
average_spending_scores = []

# Report file
report_file = os.path.join(
    output_folder,
    "profiling_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("CUSTOMER SEGMENT PROFILING REPORT\n")
    report.write("=" * 45 + "\n\n")

    # Process one cluster at a time
    for cluster_number in cluster_list:

        # Select customers of the current cluster
        cluster_data = customer_data[
            customer_data["Cluster"] == cluster_number
        ]

        # Count customers
        customer_count = len(cluster_data)

        # Calculate average income
        average_income = cluster_data["AnnualIncome"].mean()

        # Calculate average spending score
        average_spending = cluster_data["SpendingScore"].mean()

        # Store values in lists
        cluster_numbers.append(cluster_number)
        customer_counts.append(customer_count)
        average_incomes.append(round(average_income, 2))
        average_spending_scores.append(round(average_spending, 2))

        # Write cluster details
        report.write("Cluster ")
        report.write(str(cluster_number))
        report.write("\n")

        report.write("--------------------\n")

        report.write("Customers : ")
        report.write(str(customer_count))
        report.write("\n")

        report.write("Average Income : ")
        report.write(str(round(average_income, 2)))
        report.write("\n")

        report.write("Average Spending Score : ")
        report.write(str(round(average_spending, 2)))
        report.write("\n\n")

    # Final conclusion
    report.write("Conclusion\n")
    report.write("--------------------\n")
    report.write(
        "Each customer segment has different income "
        "and spending behaviour. These profiles help "
        "businesses understand their customers better."
    )

# Create a table from the collected lists
profile_table = pd.DataFrame()

profile_table["Cluster"] = cluster_numbers
profile_table["Customers"] = customer_counts
profile_table["AverageIncome"] = average_incomes
profile_table["AverageSpendingScore"] = average_spending_scores

# Save the profile table
profile_file = os.path.join(
    output_folder,
    "customer_profiles.csv"
)

profile_table.to_csv(
    profile_file,
    index=False
)

print("Customer profiling completed successfully.")
print("Profile file saved in:", profile_file)
print("Report saved in:", report_file)