# ==========================================================
# Project 11 - Loan Approval Prediction using Decision Tree
# ==========================================================

# -----------------------------
# Step 1: Import Required Libraries
# -----------------------------
import os

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier


# -----------------------------
# Step 2: Create Folder Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

DATA_FILE = os.path.join(DATA_FOLDER, "loan_data.csv")


# -----------------------------
# Step 3: Load Dataset
# -----------------------------
print("=" * 50)
print("Loan Approval Prediction Project")
print("=" * 50)

print("\nLoading dataset...")

loan_data = pd.read_csv(DATA_FILE)

print("Dataset loaded successfully.\n")


# -----------------------------
# Step 4: Display Dataset Information
# -----------------------------
print("First Five Rows\n")
print(loan_data.head())

print("\nDataset Shape")
print(loan_data.shape)

print("\nColumn Names")
print(list(loan_data.columns))

print("\nDataset Information")
print(loan_data.info())

print("\nMissing Values")
print(loan_data.isnull().sum())


# -----------------------------
# Step 5: Handle Missing Values
# -----------------------------
print("\nHandling missing values...")

text_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

numeric_columns = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

for column in text_columns:
    loan_data[column] = loan_data[column].fillna(
        loan_data[column].mode()[0]
    )

for column in numeric_columns:
    loan_data[column] = loan_data[column].fillna(
        loan_data[column].median()
    )

print("Missing values handled successfully.")

# -----------------------------
# Step 6: Convert Text into Numbers
# -----------------------------
print("\nEncoding categorical columns...")

encoder = LabelEncoder()

loan_data["Gender"] = encoder.fit_transform(loan_data["Gender"])
loan_data["Married"] = encoder.fit_transform(loan_data["Married"])
loan_data["Dependents"] = encoder.fit_transform(loan_data["Dependents"])
loan_data["Education"] = encoder.fit_transform(loan_data["Education"])
loan_data["Self_Employed"] = encoder.fit_transform(loan_data["Self_Employed"])
loan_data["Property_Area"] = encoder.fit_transform(loan_data["Property_Area"])
loan_data["Loan_Status"] = encoder.fit_transform(loan_data["Loan_Status"])

print("Encoding completed.")

# -----------------------------
# Step 7: Exploratory Data Analysis
# -----------------------------

# Graph 1
plt.figure(figsize=(6,4))

loan_data["Loan_Status"].value_counts().plot(
    kind="bar"
)

plt.title("Loan Approval Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "loan_status_distribution.png"
    )
)

plt.close()


# Graph 2
plt.figure(figsize=(6,4))

loan_data["ApplicantIncome"].plot(
    kind="hist",
    bins=20
)

plt.title("Applicant Income Distribution")
plt.xlabel("Income")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "income_distribution.png"
    )
)

plt.close()

# Graph 3
plt.figure(figsize=(6,4))

loan_data["LoanAmount"].plot(
    kind="hist",
    bins=20
)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "loan_amount_distribution.png"
    )
)

plt.close()


# Graph 4
plt.figure(figsize=(6,4))

loan_data["Education"].value_counts().plot(
    kind="bar"
)

plt.title("Education Distribution")
plt.xlabel("Education")
plt.ylabel("Number of Applicants")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "education_distribution.png"
    )
)

plt.close()


# -----------------------------
# Step 8: Prepare Features and Target
# -----------------------------

X = loan_data.drop(
    columns=["Loan_ID", "Loan_Status"]
)

y = loan_data["Loan_Status"]


# -----------------------------
# Step 9: Split Dataset
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining samples :", len(X_train))
print("Testing samples  :", len(X_test))



# -----------------------------
# Step 10: Create Decision Tree Model
# -----------------------------
print("\nCreating Decision Tree model...")

model = DecisionTreeClassifier(
    random_state=42
)

# -----------------------------
# Step 11: Train the Model
# -----------------------------
print("Training the model...")

model.fit(
    X_train,
    y_train
)

print("Model trained successfully.")


# -----------------------------
# Step 12: Make Predictions
# -----------------------------
print("\nMaking predictions...")

predictions = model.predict(
    X_test
)

print("Predictions completed.")


# -----------------------------
# Step 13: Calculate Accuracy
# -----------------------------
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nModel Accuracy : {accuracy:.2%}")


# -----------------------------
# Step 14: Confusion Matrix
# -----------------------------
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(
    y_test,
    predictions
)

print("\nConfusion Matrix")
print(confusion)


# -----------------------------
# Step 15: Classification Report
# -----------------------------
from sklearn.metrics import classification_report

classification_text = classification_report(
    y_test,
    predictions
)

print("\nClassification Report")
print(classification_text)


# -----------------------------
# Step 16: Feature Importance
# -----------------------------
importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print(importance)


plt.figure(figsize=(8,5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.xticks(rotation=45)

plt.title("Feature Importance")

plt.xlabel("Features")

plt.ylabel("Importance")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "feature_importance.png"
    )
)

plt.close()


# -----------------------------
# Step 17: Save Predictions
# -----------------------------
prediction_results = X_test.copy()

prediction_results["Actual_Loan_Status"] = y_test.values

prediction_results["Predicted_Loan_Status"] = predictions

prediction_file = os.path.join(
    OUTPUT_FOLDER,
    "predictions.csv"
)

prediction_results.to_csv(
    prediction_file,
    index=False
)

print("\nPredictions saved successfully.")



# -----------------------------
# Step 18: Generate Project Report
# -----------------------------
report_file = os.path.join(
    OUTPUT_FOLDER,
    "project_report.txt"
)

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 50 + "\n")
    file.write("Loan Approval Prediction Project Report\n")
    file.write("=" * 50 + "\n\n")

    file.write("Dataset Summary\n")
    file.write("-----------------------------\n")
    file.write(f"Total Records : {loan_data.shape[0]}\n")
    file.write(f"Total Columns : {loan_data.shape[1]}\n\n")

    file.write("Model Used\n")
    file.write("-----------------------------\n")
    file.write("Decision Tree Classifier\n\n")

    file.write("Model Performance\n")
    file.write("-----------------------------\n")
    file.write(f"Accuracy : {accuracy:.2%}\n\n")

    file.write("Confusion Matrix\n")
    file.write("-----------------------------\n")
    file.write(f"{confusion}\n\n")

    file.write("Classification Report\n")
    file.write("-----------------------------\n")
    file.write(classification_text + "\n")

    file.write("Top Important Features\n")
    file.write("-----------------------------\n")

    for _, row in importance.head(5).iterrows():
        file.write(
            f"{row['Feature']} : {row['Importance']:.4f}\n"
        )

    file.write("\nProject completed successfully.\n")


# -----------------------------
# Step 19: Display Summary
# -----------------------------
print("\n" + "=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 50)

print(f"\nModel Accuracy : {accuracy:.2%}")

print("\nOutput Files Generated")

print("--------------------------------")
print("Predictions CSV")
print(prediction_file)

print("\nProject Report")
print(report_file)

print("\nGraphs")

print(
    os.path.join(
        OUTPUT_FOLDER,
        "loan_status_distribution.png"
    )
)

print(
    os.path.join(
        OUTPUT_FOLDER,
        "income_distribution.png"
    )
)

print(
    os.path.join(
        OUTPUT_FOLDER,
        "loan_amount_distribution.png"
    )
)

print(
    os.path.join(
        OUTPUT_FOLDER,
        "education_distribution.png"
    )
)

print(
    os.path.join(
        OUTPUT_FOLDER,
        "feature_importance.png"
    )
)

print("\nThank you for using this project!")