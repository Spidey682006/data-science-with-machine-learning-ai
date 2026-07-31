import os

import pandas as pd


# Find the main project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "business_sales.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create the outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the dataset
sales_data = pd.read_csv(data_file)

# Get all business categories
category_list = sales_data["Category"].unique()
category_list = sorted(category_list)

# Create lists to store summary information
categories = []
total_sales = []
product_counts = []

# Create the report
report_file = os.path.join(
    output_folder,
    "business_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("BUSINESS FIRST DATA SCIENCE REPORT\n")
    report.write("=" * 45 + "\n\n")

    # Process one category at a time
    for category_name in category_list:

        # Select products of the current category
        category_data = sales_data[
            sales_data["Category"] == category_name
        ]

        # Count products
        number_of_products = len(category_data)

        # Calculate total sales
        sales_amount = category_data["Sales"].sum()

        # Store the results
        categories.append(category_name)
        total_sales.append(sales_amount)
        product_counts.append(number_of_products)

        # Write category details
        report.write("Category : ")
        report.write(category_name)
        report.write("\n")

        report.write("--------------------\n")

        report.write("Products : ")
        report.write(str(number_of_products))
        report.write("\n")

        report.write("Total Sales : ")
        report.write(str(sales_amount))
        report.write("\n\n")

    report.write("Conclusion\n")
    report.write("--------------------\n")
    report.write(
        "The business analysis summarizes the sales "
        "performance of each product category. "
        "This information helps businesses understand "
        "which categories generate higher sales."
    )

# Create summary table
summary_table = pd.DataFrame()

summary_table["Category"] = categories
summary_table["Products"] = product_counts
summary_table["TotalSales"] = total_sales

# Save summary table
summary_file = os.path.join(
    output_folder,
    "business_summary.csv"
)

summary_table.to_csv(
    summary_file,
    index=False
)

print("Business analysis completed successfully.")
print("Summary file saved in:", summary_file)
print("Report saved in:", report_file)