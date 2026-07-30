# Project 01 — Business Problem Framing

## Overview

Business Problem Framing is the first and one of the most important steps in every Data Science and Machine Learning project. Before building a model, it is essential to understand the business objective, determine whether Machine Learning is actually required, identify the available data, and define success metrics.

This project implements a **Business Problem Analyzer**, a command-line Python application that helps convert a business problem into a structured Machine Learning problem statement.

## Objectives

* Understand business requirements
* Identify whether ML is appropriate
* Recommend the correct ML approach
* Define required data
* Identify target variables
* Recommend evaluation metrics
* Highlight risks and ethical considerations
* Architecture diagram
* Execution flow
* Future roadmap
* Example output

## Features

* Interactive command-line interface
* Business problem analysis
* Machine Learning feasibility assessment
* Recommendation of ML task
* Structured project summary
* Export results to JSON and text files

## Project Structure

```text
01-business-problem-framing/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
├── data/
├── outputs/
├── assets/
└── tests/
```

## Requirements

* Python 3.10 or later

## Installation

```bash
git clone <repository-url>
cd 01-business-problem-framing
```

## Run

```bash
python src/main.py
```

## Expected Output

The application generates:

* Business summary
* ML recommendation
* Suggested algorithm category
* Required dataset
* Success metrics
* Ethical considerations

The generated reports are stored inside the `outputs` directory.

## License

MIT License.

