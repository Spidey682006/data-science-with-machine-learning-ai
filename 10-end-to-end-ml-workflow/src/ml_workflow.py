import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Find the main project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "student_scores.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the dataset
student_data = pd.read_csv(data_file)

# Select the input columns (features)
input_data = student_data[["HoursStudied", "Attendance"]]

# Select the output column (target)
target_data = student_data["Passed"]

# Divide the dataset into training and testing data
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

# Predict the testing data
predicted_result = decision_tree.predict(
    testing_input
)

# Create a copy of the testing data
prediction_table = testing_input.copy()

# Store actual and predicted values
actual_result = list(testing_output)
predicted_list = list(predicted_result)

prediction_table["Actual"] = actual_result
prediction_table["Predicted"] = predicted_list

# Save the prediction table
prediction_file = os.path.join(
    output_folder,
    "predictions.csv"
)

prediction_table.to_csv(
    prediction_file,
    index=False
)

# Create the workflow report
report_file = os.path.join(
    output_folder,
    "workflow_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("END TO END MACHINE LEARNING WORKFLOW\n")
    report.write("=" * 45 + "\n\n")

    report.write("Dataset Information\n")
    report.write("-------------------\n")
    report.write("Total Records : ")
    report.write(str(len(student_data)))
    report.write("\n\n")

    report.write("Workflow Steps\n")
    report.write("-------------------\n")
    report.write("1. Read the dataset.\n")
    report.write("2. Selected the input columns.\n")
    report.write("3. Selected the target column.\n")
    report.write("4. Split the data into training and testing sets.\n")
    report.write("5. Created a Decision Tree model.\n")
    report.write("6. Trained the model.\n")
    report.write("7. Predicted the testing data.\n")
    report.write("8. Saved the prediction results.\n\n")

    report.write("Conclusion\n")
    report.write("-------------------\n")
    report.write(
        "The complete machine learning workflow was "
        "performed successfully from reading the data "
        "to generating predictions."
    )

print("Machine learning workflow completed successfully.")
print("Prediction file saved in:", prediction_file)
print("Workflow report saved in:", report_file)