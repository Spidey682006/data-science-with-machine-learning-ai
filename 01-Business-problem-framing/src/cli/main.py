"""
Project 01 - Business Problem Framing

Entry point of the application.
"""

from analyzer import BusinessProblemAnalyzer
from exporter import ResultExporter
from models import BusinessProblem
from validator import ValidationError, validate_problem


def main() -> None:

    print("=" * 60)
    print("Business Problem Analyzer")
    print("=" * 60)

    try:

        problem = BusinessProblem(

            domain=input("Business Domain: "),

            title=input("Problem Title: "),

            description=input(
                "Problem Description: "
            ),

            current_process=input(
                "Current Process: "
            ),

            desired_outcome=input(
                "Desired Outcome: "
            ),
        )

        validate_problem(problem)

        analyzer = BusinessProblemAnalyzer()

        result = analyzer.analyze(problem)

        print("\nAnalysis Complete\n")

        print(f"ML Required : {result.ml_required}")

        print(
            f"Task        : {result.recommended_task.value}"
        )

        exporter = ResultExporter()

        exporter.export(problem, result)

        print(
            "\nResults exported to outputs/ directory."
        )

    except ValidationError as error:

        print(f"\nValidation Error: {error}")

    except KeyboardInterrupt:

        print("\nOperation cancelled.")

    except Exception as error:

        print(f"\nUnexpected Error: {error}")


if __name__ == "__main__":
    main()
