# Project 03 – Data Cleaning & Preparation

## Objective

Prepare a raw dataset for analysis using NumPy and Pandas by cleaning missing values, removing duplicate records, standardizing text fields, and applying basic data transformations.

---

## Concepts Covered

- NumPy
- Pandas DataFrame
- CSV Processing
- Missing Value Handling
- Duplicate Removal
- Data Transformation
- Data Cleaning

---

## Project Structure

```text
03-data-cleaning-preparation/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── customers.csv
│   └── cleaned/
│       └── customers_cleaned.csv
│
├── outputs/
│   └── cleaning_summary.txt
│
└── src/
    └── clean_data.py
```

---

## Cleaning Steps

- Remove duplicate records
- Handle missing values
- Standardize names and cities
- Trim whitespace
- Create a customer segment column

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python src/clean_data.py
```

---

## Generated Files

After execution:

```text
data/cleaned/customers_cleaned.csv
outputs/cleaning_summary.txt
```

---

## Conclusion

The dataset is transformed into a clean and consistent format suitable for further exploratory data analysis and machine learning tasks.
