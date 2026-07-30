"""
Project 01 - Business Problem Framing

Application constants and predefined values.
"""

from enum import Enum


class MLTask(Enum):
    """Supported Machine Learning task types."""

    CLASSIFICATION = "Classification"
    REGRESSION = "Regression"
    CLUSTERING = "Clustering"
    ANOMALY_DETECTION = "Anomaly Detection"
    RECOMMENDATION = "Recommendation"
    RULE_BASED = "Rule-Based Solution"
    NOT_REQUIRED = "Machine Learning Not Required"


class EvaluationMetric(Enum):
    """Common evaluation metrics."""

    ACCURACY = "Accuracy"
    PRECISION = "Precision"
    RECALL = "Recall"
    F1_SCORE = "F1 Score"
    RMSE = "Root Mean Squared Error (RMSE)"
    MAE = "Mean Absolute Error (MAE)"
    SILHOUETTE = "Silhouette Score"
    MAP = "Mean Average Precision"


BUSINESS_DOMAINS = [
    "Healthcare",
    "Finance",
    "Retail",
    "E-Commerce",
    "Education",
    "Manufacturing",
    "Agriculture",
    "Transportation",
    "Human Resources",
    "Marketing",
    "Telecommunications",
    "Government",
    "Energy",
    "Insurance",
    "Real Estate",
    "Other"
]


EXPORT_DIRECTORY = "outputs"

JSON_FILENAME = "project_summary.json"

TEXT_FILENAME = "project_summary.txt"
