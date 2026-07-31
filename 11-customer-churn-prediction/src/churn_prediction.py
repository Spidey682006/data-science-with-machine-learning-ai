import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Find the main project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "customer_churn.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create the outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the dataset
customer_data = pd.read_csv(data_file)

# Select the input columns
input_data = customer_data[[
    "Age",
    "MonthlyBill",
    "Tenure"
]]

# Select the target column
target_data = customer_data["Churn"]

# Split the dataset into training and testing data
training_input, testing_input, training_output, testing_output = train_test_split(
    input_data,
    target_data,
    test_size=0.30,
    random_state=42
)

# Create the Decision Tree model
decision_tree = DecisionTreeClassifier(
    random_state=42
)

# Train the model
decision_tree.fit(
    training_input,
    training_output
)

# Predict customer churn
predicted_result = decision_tree.predict(
    testing_input
)

# Create a new table for storing predictions
prediction_table = testing_input.copy()

# Add actual results
actual_result = list(testing_output)
prediction_table["Actual"] = actual_result

# Add predicted results
predicted_list = list(predicted_result)
prediction_table["Predicted"] = predicted_list

# Save the prediction table
prediction_file = os.path.join(
    output_folder,
    "churn_predictions.csv"
)

prediction_table.to_csv(
    prediction_file,
    index=False
)

# Count customers predicted to leave
predicted_churn = predicted_list.count("Yes")

# Count customers predicted to stay
predicted_retained = predicted_list.count("No")

# Create the report
report_file = os.path.join(
    output_folder,
    "churn_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("CUSTOMER CHURN PREDICTION REPORT\n")
    report.write("=" * 45 + "\n\n")

    report.write("Dataset Summary\n")
    report.write("--------------------\n")
    report.write("Total Customers : ")
    report.write(str(len(customer_data)))
    report.write("\n\n")

    report.write("Prediction Summary\n")
    report.write("--------------------\n")
    report.write("Customers Predicted to Leave : ")
    report.write(str(predicted_churn))
    report.write("\n")

    report.write("Customers Predicted to Stay : ")
    report.write(str(predicted_retained))
    report.write("\n\n")

    report.write("Workflow Used\n")
    report.write("--------------------\n")
    report.write("1. Read the customer dataset.\n")
    report.write("2. Selected the input columns.\n")
    report.write("3. Selected the target column.\n")
    report.write("4. Split the dataset into training and testing sets.\n")
    report.write("5. Created a Decision Tree model.\n")
    report.write("6. Trained the model.\n")
    report.write("7. Predicted customer churn.\n")
    report.write("8. Saved the prediction results.\n\n")

    report.write("Conclusion\n")
    report.write("--------------------\n")
    report.write(
        "The Decision Tree model predicts whether a customer "
        "is likely to leave the company by using Age, "
        "Monthly Bill, and Tenure."
    )

print("Customer churn prediction completed successfully.")
print("Prediction file saved in:", prediction_file)
print("Report saved in:", report_file)