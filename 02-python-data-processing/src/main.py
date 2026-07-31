import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
EMPLOYEE_FILE = PROJECT_ROOT / "data" / "employees.csv"
REPORT_FILE = PROJECT_ROOT / "outputs" / "report.txt"


def load_employee_records(csv_file):
    with csv_file.open(newline="", encoding="utf-8") as source:
        employee_records = []

        for employee in csv.DictReader(source):
            employee["salary"] = int(employee["salary"])
            employee["experience"] = int(employee["experience"])
            employee_records.append(employee)

    return employee_records


def build_salary_report(employee_records):
    employee_count = len(employee_records)

    average_salary = (
        sum(record["salary"] for record in employee_records)
        / employee_count
    )

    highest_paid_employee = max(
        employee_records,
        key=lambda employee: employee["salary"],
    )

    experienced_staff = [
        employee
        for employee in employee_records
        if employee["experience"] >= 5
    ]

    return {
        "employee_count": employee_count,
        "average_salary": average_salary,
        "highest_paid_employee": highest_paid_employee,
        "experienced_staff": experienced_staff,
    }


def write_report(report_summary):
    REPORT_FILE.parent.mkdir(exist_ok=True)

    with REPORT_FILE.open("w", encoding="utf-8") as report:

        report.write("EMPLOYEE DATA REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(
            f"Total Employees : {report_summary['employee_count']}\n"
        )

        report.write(
            f"Average Salary  : {report_summary['average_salary']:.2f}\n"
        )

        top_employee = report_summary["highest_paid_employee"]

        report.write(
            f"Highest Salary  : "
            f"{top_employee['name']} "
            f"({top_employee['salary']})\n\n"
        )

        report.write("Employees with 5+ Years Experience\n")
        report.write("-" * 40 + "\n")

        for employee in report_summary["experienced_staff"]:
            report.write(
                f"{employee['name']} "
                f"({employee['department']})\n"
            )


if __name__ == "__main__":
    try:
        employee_records = load_employee_records(EMPLOYEE_FILE)
        salary_report = build_salary_report(employee_records)

        print(f"Employees      : {salary_report['employee_count']}")
        print(f"Average Salary : {salary_report['average_salary']:.2f}")

        top_employee = salary_report["highest_paid_employee"]

        print(
            f"Highest Salary : "
            f"{top_employee['name']} "
            f"({top_employee['salary']})"
        )

        write_report(salary_report)

        print(f"Report saved to {REPORT_FILE}")

    except FileNotFoundError:
        print(f"Dataset not found: {EMPLOYEE_FILE}")

    except Exception as exc:
        print(exc)
