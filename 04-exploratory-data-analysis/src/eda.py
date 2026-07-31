from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


project_folder = Path(__file__).resolve().parent.parent

data_file = project_folder / "data" / "customers.csv"
output_folder = project_folder / "outputs"
chart_folder = output_folder / "charts"

output_folder.mkdir(parents=True, exist_ok=True)
chart_folder.mkdir(parents=True, exist_ok=True)

customers = pd.read_csv(data_file)

total_customers = len(customers)

statistics = customers.describe()

city_count = customers["city"].value_counts()

summary_path = output_folder / "eda_summary.txt"

with open(summary_path, "w", encoding="utf-8") as report:

    report.write("EXPLORATORY DATA ANALYSIS\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Total Customers : {total_customers}\n\n")

    report.write("Numerical Summary\n")
    report.write("-" * 40 + "\n")
    report.write(statistics.to_string())
    report.write("\n\n")

    report.write("Customers by City\n")
    report.write("-" * 40 + "\n")
    report.write(city_count.to_string())


plt.figure(figsize=(6, 4))
plt.hist(customers["age"], bins=6)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(chart_folder / "age_distribution.png")
plt.close()


plt.figure(figsize=(6, 4))
customers["city"].value_counts().plot(kind="bar")
plt.title("Customers by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(chart_folder / "city_distribution.png")
plt.close()


plt.figure(figsize=(6, 4))
plt.hist(customers["purchase_amount"], bins=6)
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(chart_folder / "purchase_distribution.png")
plt.close()


plt.figure(figsize=(5, 5))
customers["gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(chart_folder / "gender_distribution.png")
plt.close()


print("EDA completed successfully.")
print(f"Records analysed : {total_customers}")
print(f"Summary saved to : {summary_path}")
print(f"Charts saved in  : {chart_folder}")