"""
Project 01 - Business Problem Framing

Core business analysis engine.
"""

from constants import MLTask, EvaluationMetric
from models import BusinessProblem, AnalysisResult


class BusinessProblemAnalyzer:
    """
    Analyzes a business problem and recommends
    an appropriate Machine Learning approach.
    """

    def analyze(
        self,
        problem: BusinessProblem
    ) -> AnalysisResult:

        description = (
            problem.description +
            " " +
            problem.desired_outcome
        ).lower()

        if any(
            word in description
            for word in [
                "predict",
                "forecast",
                "estimate"
            ]
        ):

            return self._classification_or_regression(problem)

        if any(
            word in description
            for word in [
                "group",
                "cluster",
                "segment"
            ]
        ):

            return self._clustering(problem)

        if any(
            word in description
            for word in [
                "recommend",
                "suggest"
            ]
        ):

            return self._recommendation(problem)

        return self._rule_based(problem)

    def _classification_or_regression(
        self,
        problem: BusinessProblem
    ) -> AnalysisResult:

        description = problem.description.lower()

        regression_words = [
            "price",
            "sales",
            "revenue",
            "temperature",
            "cost",
            "amount"
        ]

        if any(word in description for word in regression_words):

            return AnalysisResult(
                ml_required=True,
                recommended_task=MLTask.REGRESSION,
                required_data=[
                    "Historical records",
                    "Relevant numerical features"
                ],
                evaluation_metrics=[
                    EvaluationMetric.RMSE.value,
                    EvaluationMetric.MAE.value
                ],
                recommendations=[
                    "Collect historical numerical data.",
                    "Evaluate regression performance."
                ]
            )

        return AnalysisResult(
            ml_required=True,
            recommended_task=MLTask.CLASSIFICATION,
            required_data=[
                "Historical labeled data"
            ],
            evaluation_metrics=[
                EvaluationMetric.ACCURACY.value,
                EvaluationMetric.F1_SCORE.value
            ],
            recommendations=[
                "Create labeled training data.",
                "Evaluate class balance."
            ]
        )

    def _clustering(
        self,
        problem: BusinessProblem
    ) -> AnalysisResult:

        return AnalysisResult(
            ml_required=True,
            recommended_task=MLTask.CLUSTERING,
            required_data=[
                "Customer or entity attributes"
            ],
            evaluation_metrics=[
                EvaluationMetric.SILHOUETTE.value
            ],
            recommendations=[
                "Normalize features.",
                "Experiment with different cluster counts."
            ]
        )

    def _recommendation(
        self,
        problem: BusinessProblem
    ) -> AnalysisResult:

        return AnalysisResult(
            ml_required=True,
            recommended_task=MLTask.RECOMMENDATION,
            required_data=[
                "User interaction history",
                "Product metadata"
            ],
            evaluation_metrics=[
                EvaluationMetric.MAP.value
            ],
            recommendations=[
                "Collect user behavior.",
                "Build recommendation engine."
            ]
        )

    def _rule_based(
        self,
        problem: BusinessProblem
    ) -> AnalysisResult:

        return AnalysisResult(
            ml_required=False,
            recommended_task=MLTask.RULE_BASED,
            recommendations=[
                "Machine Learning is not currently necessary.",
                "Consider automating with business rules."
            ]
        )
