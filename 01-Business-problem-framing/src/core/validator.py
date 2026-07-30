"""
Project 01 - Business Problem Framing

Input validation utilities.
"""

from models import BusinessProblem
from constants import BUSINESS_DOMAINS


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def validate_non_empty(field_name: str, value: str) -> str:
    """
    Ensures that a string field is not empty.
    """

    value = value.strip()

    if not value:
        raise ValidationError(f"{field_name} cannot be empty.")

    return value


def validate_domain(domain: str) -> str:
    """
    Validates the selected business domain.
    """

    domain = validate_non_empty("Business Domain", domain)

    if domain not in BUSINESS_DOMAINS:
        raise ValidationError(
            f"Unsupported business domain: '{domain}'."
        )

    return domain


def validate_problem(problem: BusinessProblem) -> BusinessProblem:
    """
    Validates an entire BusinessProblem object.
    """

    problem.domain = validate_domain(problem.domain)

    problem.title = validate_non_empty(
        "Problem Title",
        problem.title
    )

    problem.description = validate_non_empty(
        "Problem Description",
        problem.description
    )

    problem.current_process = validate_non_empty(
        "Current Process",
        problem.current_process
    )

    problem.desired_outcome = validate_non_empty(
        "Desired Outcome",
        problem.desired_outcome
    )

    return problem
