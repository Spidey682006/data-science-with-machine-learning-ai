import os

import pandas as pd
from sklearn.linear_model import LinearRegression


# Find the main project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "sales_data.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create the outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the sales dataset
sales_data = pd.read_csv(data_file)

# Select the input column
input_data = sales_data[["Month"]]

# Select the output column
target_data = sales_data["Sales"]

# Create the Linear Regression model
linear_model = LinearRegression()

# Train the model
linear_model.fit(
    input_data,
    target_data
)

# Create a table for future months
future_months = pd.DataFrame()

future_months["Month"] = [13, 14, 15]

# Predict future sales
predicted_sales = linear_model.predict(
    future_months
)

# Round the predicted values
rounded_sales = []

for sale in predicted_sales:
    rounded_sales.append(round(sale, 2))

# Create another table for saving predictions
forecast_table = future_months.copy()

forecast_table["PredictedSales"] = rounded_sales

# Save the forecast table
forecast_file = os.path.join(
    output_folder,
    "sales_forecast.csv"
)

forecast_table.to_csv(
    forecast_file,
    index=False
)

# Create the report
report_file = os.path.join(
    output_folder,
    "forecast_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("SALES DEMAND FORECAST REPORT\n")
    report.write("=" * 45 + "\n\n")

    report.write("Dataset Summary\n")
    report.write("--------------------\n")
    report.write("Total Months : ")
    report.write(str(len(sales_data)))
    report.write("\n\n")

    report.write("Forecast Results\n")
    report.write("--------------------\n")

    month_list = list(future_months["Month"])

    for i in range(len(month_list)):

        report.write("Month ")
        report.write(str(month_list[i]))
        report.write(" : ")

        report.write(str(rounded_sales[i]))
        report.write("\n")

    report.write("\n")

    report.write("Workflow Used\n")
    report.write("--------------------\n")
    report.write("1. Read the sales dataset.\n")
    report.write("2. Selected the input column.\n")
    report.write("3. Selected the output column.\n")
    report.write("4. Created a Linear Regression model.\n")
    report.write("5. Trained the model.\n")
    report.write("6. Predicted future sales.\n")
    report.write("7. Saved the forecast results.\n\n")

    report.write("Conclusion\n")
    report.write("--------------------\n")
    report.write(
        "The Linear Regression model used historical "
        "sales data to estimate future sales."
    )

print("Sales forecasting completed successfully.")
print("Forecast file saved in:", forecast_file)
print("Report saved in:", report_file)