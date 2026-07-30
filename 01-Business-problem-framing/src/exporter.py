"""
Project 01 - Business Problem Framing

Exports analysis results to JSON and text files.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from constants import EXPORT_DIRECTORY, JSON_FILENAME, TEXT_FILENAME
from models import BusinessProblem, AnalysisResult


class ResultExporter:
    """Handles exporting analysis results."""

    def __init__(self) -> None:
        self.output_directory = Path(EXPORT_DIRECTORY)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def export(
        self,
        problem: BusinessProblem,
        result: AnalysisResult,
    ) -> None:
        """Export analysis to both JSON and text."""

        self._export_json(problem, result)
        self._export_text(problem, result)

    def _export_json(
        self,
        problem: BusinessProblem,
        result: AnalysisResult,
    ) -> None:

        output = {
            "generated_at": datetime.now().isoformat(),
            "business_problem": asdict(problem),
            "analysis": {
                "ml_required": result.ml_required,
                "recommended_task": result.recommended_task.value,
                "required_data": result.required_data,
                "target_variable": result.target_variable,
                "suggested_features": result.suggested_features,
                "evaluation_metrics": result.evaluation_metrics,
                "ethical_considerations": result.ethical_considerations,
                "business_kpis": result.business_kpis,
                "recommendations": result.recommendations,
            },
        }

        file_path = self.output_directory / JSON_FILENAME

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(output, file, indent=4)

    def _export_text(
        self,
        problem: BusinessProblem,
        result: AnalysisResult,
    ) -> None:

        file_path = self.output_directory / TEXT_FILENAME

        with open(file_path, "w", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write("BUSINESS PROBLEM ANALYSIS\n")
            file.write("=" * 60 + "\n\n")

            file.write(f"Domain : {problem.domain}\n")
            file.write(f"Title  : {problem.title}\n\n")

            file.write("Description\n")
            file.write(f"{problem.description}\n\n")

            file.write("Current Process\n")
            file.write(f"{problem.current_process}\n\n")

            file.write("Desired Outcome\n")
            file.write(f"{problem.desired_outcome}\n\n")

            file.write("-" * 60 + "\n")

            file.write(
                f"Machine Learning Required : {result.ml_required}\n"
            )

            file.write(
                f"Recommended Task          : {result.recommended_task.value}\n\n"
            )

            if result.required_data:
                file.write("Required Data\n")
                for item in result.required_data:
                    file.write(f" • {item}\n")
                file.write("\n")

            if result.evaluation_metrics:
                file.write("Evaluation Metrics\n")
                for item in result.evaluation_metrics:
                    file.write(f" • {item}\n")
                file.write("\n")

            if result.recommendations:
                file.write("Recommendations\n")
                for item in result.recommendations:
                    file.write(f" • {item}\n")
