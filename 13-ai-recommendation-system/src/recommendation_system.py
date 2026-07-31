import os

import pandas as pd


# Find the main project folder
project_folder = os.path.dirname(os.path.dirname(__file__))

# File locations
data_file = os.path.join(project_folder, "data", "products.csv")
output_folder = os.path.join(project_folder, "outputs")

# Create the outputs folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read the product dataset
product_data = pd.read_csv(data_file)

# Category selected by the user
preferred_category = "Electronics"

# Select products from the preferred category
electronics_products = product_data[
    product_data["Category"] == preferred_category
]

# Arrange products from highest rating to lowest rating
recommended_products = electronics_products.sort_values(
    "Rating",
    ascending=False
)

# Count recommended products
number_of_products = len(recommended_products)

# Save the recommendation table
recommendation_file = os.path.join(
    output_folder,
    "recommended_products.csv"
)

recommended_products.to_csv(
    recommendation_file,
    index=False
)

# Create the report
report_file = os.path.join(
    output_folder,
    "recommendation_report.txt"
)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("AI RECOMMENDATION SYSTEM REPORT\n")
    report.write("=" * 45 + "\n\n")

    report.write("Selected Category\n")
    report.write("--------------------\n")
    report.write(preferred_category)
    report.write("\n\n")

    report.write("Recommended Products : ")
    report.write(str(number_of_products))
    report.write("\n\n")

    report.write("Workflow Used\n")
    report.write("--------------------\n")
    report.write("1. Read the product dataset.\n")
    report.write("2. Selected the preferred category.\n")
    report.write("3. Filtered products from that category.\n")
    report.write("4. Sorted the products by rating.\n")
    report.write("5. Saved the recommended products.\n\n")

    report.write("Conclusion\n")
    report.write("--------------------\n")
    report.write(
        "The recommendation system selected products "
        "from the chosen category and displayed the "
        "highest-rated products first."
    )

print("Recommendation system completed successfully.")
print("Recommendation file saved in:", recommendation_file)
print("Report saved in:", report_file)