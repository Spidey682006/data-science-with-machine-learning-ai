# Project 01 – Business Problem Framing

## Course

Data Science with Machine Learning & Artificial Intelligence Internship

## Project Objective

The objective of this project is to understand how a business problem is identified, analyzed, and converted into a Data Science or Machine Learning problem before any model development begins.

Business Problem Framing is the first phase of every successful Data Science project. It focuses on understanding business requirements, defining objectives, identifying available data, evaluating whether Machine Learning is required, and determining measurable success criteria.

---

# Learning Outcomes

After completing this project, the learner should be able to:

* Understand business requirements.
* Identify real-world business problems.
* Convert business objectives into analytical objectives.
* Determine whether Machine Learning is necessary.
* Select an appropriate Machine Learning approach.
* Define success metrics.
* Identify business risks and ethical considerations.

---

# Business Problem

## Problem Statement

A retail company experiences a high number of customers who stop purchasing after their first order. The company wants to identify customers who are likely to leave so that promotional offers can be provided before they stop purchasing.

---

# Business Objective

Reduce customer churn and improve customer retention through data-driven decision making.

---

# Analytical Objective

Predict whether an existing customer is likely to discontinue purchasing within the next three months.

---

# Available Data

The organization currently stores the following information:

* Customer ID
* Age
* Gender
* Location
* Purchase History
* Total Orders
* Total Spending
* Average Order Value
* Last Purchase Date
* Customer Feedback
* Membership Status

---

# Data Availability Assessment

| Requirement         | Status         |
| ------------------- | -------------- |
| Historical Data     | Available      |
| Customer Records    | Available      |
| Transaction History | Available      |
| Target Variable     | Can be Created |
| Data Volume         | Sufficient     |

---

# Is Machine Learning Required?

**Yes**

Reason:

The organization needs to predict future customer behavior based on historical data. This prediction cannot be achieved effectively using simple rule-based systems because customer behavior depends on multiple variables.

---

# Recommended Machine Learning Approach

**Problem Type**

Classification

Reason:

The output belongs to one of two categories:

* Customer Will Churn
* Customer Will Not Churn

---

# Possible Features

* Age
* Purchase Frequency
* Average Spending
* Membership Type
* Customer Location
* Time Since Last Purchase
* Number of Orders

---

# Target Variable

Customer Churn

Possible Values:

* Yes
* No

---

# Success Metrics

Business Metrics

* Reduced customer churn
* Increased customer retention
* Higher repeat purchases
* Improved customer lifetime value

Machine Learning Metrics

* Accuracy
* Precision
* Recall
* F1-Score

---

# Risks

* Incomplete customer records
* Missing purchase history
* Imbalanced dataset
* Incorrect customer labels

---

# Ethical Considerations

* Protect customer privacy.
* Use customer data responsibly.
* Avoid discriminatory predictions.
* Follow applicable data protection policies.

---

# Expected Outcome

The completed Business Problem Framing exercise provides a clear understanding of:

* The business problem.
* Business objectives.
* Analytical objectives.
* Required data.
* Machine Learning feasibility.
* Recommended Machine Learning approach.
* Evaluation metrics.
* Risks and ethical considerations.

This document serves as the foundation for subsequent stages including data collection, data preprocessing, exploratory data analysis, model development, evaluation, and deployment.

---

# Conclusion

Business Problem Framing is the foundation of every successful Data Science project. Clearly defining the business objective before collecting or analyzing data helps ensure that Machine Learning is applied only where it delivers measurable business value. This project demonstrates the systematic process of transforming a real-world business challenge into a structured analytical problem that can be solved using Data Science techniques.
