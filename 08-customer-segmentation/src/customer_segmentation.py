import os

import pandas as pd
from sklearn.cluster import KMeans


# Find the main project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "mall_customers.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the customer dataset
customers = pd.read_csv(data_file)

# Select the columns used for clustering
income = customers["AnnualIncome"]
spending = customers["SpendingScore"]

# Create a new table using only these two columns
clustering_data = pd.DataFrame()

clustering_data["AnnualIncome"] = income
clustering_data["SpendingScore"] = spending

# Create the K-Means model
kmeans_model = KMeans(
    n_clusters=3,
    random_state=42
)

# Find customer groups
cluster_numbers = kmeans_model.fit_predict(clustering_data)

# Add the cluster number to the dataset
customers["Cluster"] = cluster_numbers

# Save the updated dataset
segment_file = os.path.join(
    output_folder,
    "customer_segments.csv"
)

customers.to_csv(segment_file, index=False)

# Count customers in each cluster
cluster_count = customers["Cluster"].value_counts()
cluster_count = cluster_count.sort_index()

# Create the report
report_file = os.path.join(
    output_folder,
    "segmentation_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("CUSTOMER SEGMENTATION REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write("Total Customers : ")
    report.write(str(len(customers)))
    report.write("\n\n")

    report.write("Number of Clusters : 3\n\n")

    for cluster in cluster_count.index:

        report.write("Cluster ")
        report.write(str(cluster))
        report.write("\n")

        report.write("Customers : ")
        report.write(str(cluster_count[cluster]))
        report.write("\n\n")

    report.write("Conclusion\n")
    report.write("-" * 20 + "\n")

    report.write(
        "Customers are divided into three groups "
        "based on Annual Income and Spending Score."
    )

print("Customer segmentation completed.")
print("Segmented data saved in:", segment_file)
print("Report saved in:", report_file)