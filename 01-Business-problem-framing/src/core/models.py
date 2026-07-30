"""
Project 01 - Business Problem Framing

Application data models.
"""

from dataclasses import dataclass, field
from typing import List

from constants import MLTask


@dataclass
class BusinessProblem:
    """
    Represents the user's business problem.
    """

    domain: str
    title: str
    description: str
    current_process: str
    desired_outcome: str


@dataclass
class AnalysisResult:
    """
    Represents the generated ML analysis.
    """

    ml_required: bool

    recommended_task: MLTask

    required_data: List[str] = field(default_factory=list)

    target_variable: str = ""

    suggested_features: List[str] = field(default_factory=list)

    evaluation_metrics: List[str] = field(default_factory=list)

    ethical_considerations: List[str] = field(default_factory=list)

    business_kpis: List[str] = field(default_factory=list)

    recommendations: List[str] = field(default_factory=list)
