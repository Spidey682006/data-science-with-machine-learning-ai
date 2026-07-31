import os
import pandas as pd


# Finding project folders
project_folder = os.path.dirname(os.path.dirname(__file__))

data_path = os.path.join(project_folder, "data", "sales_data.csv")
output_path = os.path.join(project_folder, "outputs")


# Creating output folder if it does not exist
if not os.path.exists(output_path):
    os.makedirs(output_path)


# Reading sales data from CSV file
sales_data = pd.read_csv(data_path)


# Taking sales column for calculation
sales = sales_data["sales_amount"]


# Calculating basic statistics
average_sales = sales.mean()
median_sales = sales.median()
maximum_sales = sales.max()
minimum_sales = sales.min()

sales_variance = sales.var()
sales_std = sales.std()


# Finding the most sold product
product_count = sales_data["product"].value_counts()
most_sold_product = product_count.index[0]


# Finding the best performing region
region_total_sales = sales_data.groupby("region")["sales_amount"].sum()
best_region = region_total_sales.idxmax()


# Creating report file
report_path = os.path.join(output_path, "statistical_report.txt")


with open(report_path, "w") as file:

    file.write("SALES STATISTICAL REPORT\n")
    file.write("========================\n\n")


    file.write("Total Sales Records: ")
    file.write(str(len(sales_data)))
    file.write("\n\n")


    file.write("Average Sales: ")
    file.write(str(round(average_sales, 2)))
    file.write("\n")

    file.write("Median Sales: ")
    file.write(str(round(median_sales, 2)))
    file.write("\n")

    file.write("Highest Sale: ")
    file.write(str(maximum_sales))
    file.write("\n")

    file.write("Lowest Sale: ")
    file.write(str(minimum_sales))
    file.write("\n")

    file.write("Variance: ")
    file.write(str(round(sales_variance, 2)))
    file.write("\n")

    file.write("Standard Deviation: ")
    file.write(str(round(sales_std, 2)))
    file.write("\n\n")


    file.write("Most Sold Product: ")
    file.write(str(most_sold_product))
    file.write("\n")


    file.write("Best Performing Region: ")
    file.write(str(best_region))
    file.write("\n\n")


    file.write("Business Suggestions\n")
    file.write("--------------------\n")


    if average_sales > 35000:
        file.write("Sales performance is good.\n")
    else:
        file.write("Sales performance needs improvement.\n")


    file.write("Focus marketing on the best region.\n")
    file.write("Promote the most sold product.\n")
    file.write("Improve sales of low-performing products.\n")


print("Sales analysis completed.")
print("Report created at:", report_path)
