# Project 11 – Loan Approval Prediction using Decision Tree

## Objective

Build a machine learning model to predict whether a loan application will be approved based on applicant details using a Decision Tree Classifier.

---

## Topics Covered

- Data Loading
- Data Preprocessing
- Missing Value Handling
- Label Encoding
- Exploratory Data Analysis (EDA)
- Decision Tree Classification
- Train-Test Split
- Model Evaluation
- Accuracy Score
- Confusion Matrix
- Classification Report
- Feature Importance

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## Install

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python src/Loan_approval.py
```

---

## Output

```text
outputs/
├── predictions.csv
├── project_report.txt
├── loan_status_distribution.png
├── income_distribution.png
├── loan_amount_distribution.png
├── education_distribution.png
└── feature_importance.png
```

---

## Project Workflow

```text
Load Dataset
      ↓
Handle Missing Values
      ↓
Encode Categorical Data
      ↓
Perform Exploratory Data Analysis
      ↓
Split Dataset into Training and Testing Sets
      ↓
Train Decision Tree Model
      ↓
Make Predictions
      ↓
Evaluate Model Performance
      ↓
Save Results and Reports
```

---

## Conclusion

This project demonstrates a complete machine learning workflow for loan approval prediction. The dataset is cleaned, categorical features are encoded, and a Decision Tree classifier is trained to predict loan approval status. The model is evaluated using accuracy, a confusion matrix, and a classification report. The project also generates graphs, prediction results, and a summary report, making it a simple and practical example of a classification problem.
