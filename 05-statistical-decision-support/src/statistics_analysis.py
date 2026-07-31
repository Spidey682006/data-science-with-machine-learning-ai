import os

import pandas as pd


project_folder = os.path.dirname(os.path.dirname(__file__))

data_file = os.path.join(project_folder, "data", "sales_data.csv")
output_folder = os.path.join(project_folder, "outputs")

os.makedirs(output_folder, exist_ok=True)

sales_data = pd.read_csv(data_file)

sales_amount = sales_data["sales_amount"]

average_sales = sales_amount.mean()
median_sales = sales_amount.median()
highest_sales = sales_amount.max()
lowest_sales = sales_amount.min()
variance = sales_amount.var()
standard_deviation = sales_amount.std()

most_sold_product = sales_data["product"].mode()
most_sold_product = most_sold_product[0]

region_sales = sales_data.groupby("region")["sales_amount"].sum()
best_region = region_sales.idxmax()

report_file = os.path.join(output_folder, "statistical_report.txt")

with open(report_file, "w", encoding="utf-8") as report:

    report.write("STATISTICAL DECISION SUPPORT REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Total Records : {len(sales_data)}\n\n")

    report.write(f"Average Sales : {average_sales:.2f}\n")
    report.write(f"Median Sales : {median_sales:.2f}\n")
    report.write(f"Highest Sale : {highest_sales}\n")
    report.write(f"Lowest Sale : {lowest_sales}\n")
    report.write(f"Variance : {variance:.2f}\n")
    report.write(f"Standard Deviation : {standard_deviation:.2f}\n\n")

    report.write(f"Most Sold Product : {most_sold_product}\n")
    report.write(f"Best Performing Region : {best_region}\n\n")

    report.write("Business Suggestions\n")
    report.write("---------------------\n")

    if average_sales > 35000:
        report.write("Average sales are good.\n")
    else:
        report.write("Average sales should be improved.\n")

    report.write("Increase marketing in the best-performing region.\n")
    report.write("Keep promoting the most sold product.\n")
    report.write("Review products with lower sales.\n")

print("Analysis completed successfully.")
print("Report saved in:", report_file)