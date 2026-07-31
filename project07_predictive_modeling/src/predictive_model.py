import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Finding project location
project_folder = os.path.dirname(os.path.dirname(__file__))


# File locations
data_file = os.path.join(
    project_folder,
    "data",
    "customer_data.csv"
)

output_folder = os.path.join(
    project_folder,
    "outputs"
)


# Creating output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Reading dataset
data = pd.read_csv(data_file)


# Separating input and output data

features = [
    "age",
    "income",
    "website_visits",
    "previous_purchases"
]

X = data[features]

y = data["purchase"]


# Splitting data into training and testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Creating machine learning model

model = LogisticRegression()


# Training the model

model.fit(
    X_train,
    y_train
)


# Making predictions

prediction = model.predict(X_test)


# Checking accuracy

accuracy = accuracy_score(
    y_test,
    prediction
)


# Creating report

report_file = os.path.join(
    output_folder,
    "model_report.txt"
)


with open(report_file, "w") as file:

    file.write("PREDICTIVE MODEL REPORT\n")
    file.write("======================\n\n")

    file.write("Problem:\n")
    file.write("Customer Purchase Prediction\n\n")

    file.write("Machine Learning Type:\n")
    file.write("Supervised Learning\n\n")

    file.write("Algorithm Used:\n")
    file.write("Logistic Regression\n\n")

    file.write("Training Data:\n")
    file.write("80%\n\n")

    file.write("Testing Data:\n")
    file.write("20%\n\n")

    file.write("Model Accuracy:\n")
    file.write(str(round(accuracy * 100, 2)))
    file.write("%\n\n")


    if accuracy >= 0.75:
        file.write(
            "Model Performance: Good\n"
        )
    else:
        file.write(
            "Model Performance: Needs Improvement\n"
        )


    file.write("\nConclusion:\n")
    file.write(
        "The model can predict customer purchase behaviour."
    )


print("Machine learning model completed.")
print("Report saved at:", report_file)