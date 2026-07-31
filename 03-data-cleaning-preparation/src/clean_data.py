from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATASET = PROJECT_ROOT / "data" / "raw" / "customers.csv"
CLEAN_DATASET = PROJECT_ROOT / "data" / "cleaned" / "customers_cleaned.csv"
SUMMARY_FILE = PROJECT_ROOT / "outputs" / "cleaning_summary.txt"


customer_frame = pd.read_csv(RAW_DATASET)

original_records = len(customer_frame)

duplicate_records = customer_frame.duplicated().sum()

customer_frame = customer_frame.drop_duplicates()

customer_frame["name"] = (
    customer_frame["name"]
    .str.strip()
    .str.title()
)

customer_frame["city"] = (
    customer_frame["city"]
    .fillna("Unknown")
    .str.strip()
    .str.title()
)

customer_frame["gender"] = (
    customer_frame["gender"]
    .str.strip()
    .str.title()
)

customer_frame["age"] = (
    customer_frame["age"]
    .fillna(customer_frame["age"].median())
    .astype(int)
)

customer_frame["purchase_amount"] = (
    customer_frame["purchase_amount"]
    .fillna(customer_frame["purchase_amount"].mean())
    .round(2)
)

customer_frame["customer_segment"] = np.where(
    customer_frame["purchase_amount"] >= 7000,
    "Premium",
    "Standard",
)

CLEAN_DATASET.parent.mkdir(parents=True, exist_ok=True)
SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)

customer_frame.to_csv(CLEAN_DATASET, index=False)

summary = [
    "DATA CLEANING SUMMARY",
    "=" * 40,
    f"Original Records : {original_records}",
    f"Duplicate Records Removed : {duplicate_records}",
    f"Final Records : {len(customer_frame)}",
    "",
    f"Missing Age Values Filled : {customer_frame['age'].isna().sum()}",
    f"Missing City Values Filled : {customer_frame['city'].eq('Unknown').sum()}",
    "",
    "Cleaning Operations",
    "-" * 40,
    "- Removed duplicate records",
    "- Filled missing age values using median",
    "- Filled missing purchase values using mean",
    "- Filled missing cities with 'Unknown'",
    "- Trimmed whitespace",
    "- Standardized capitalization",
    "- Created customer_segment column",
]

SUMMARY_FILE.write_text("\n".join(summary), encoding="utf-8")

print("Dataset cleaned successfully.")
print(f"Rows after cleaning : {len(customer_frame)}")
print(f"Clean dataset saved : {CLEAN_DATASET}")
print(f"Summary saved       : {SUMMARY_FILE}")
