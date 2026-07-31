# Project 06 – Machine Learning Feasibility Assessment

## Objective

Evaluate whether a dataset is suitable for machine learning and recommend the appropriate learning approach.

---

## Topics Covered

- Machine Learning Basics
- Supervised Learning
- Unsupervised Learning
- Classification
- Regression
- Clustering
- Dataset Inspection

---

## Project Structure

```text
06-ml-feasibility-assessment/
│
├── data/
│   └── customer_churn.csv
│
├── outputs/
│   └── ml_feasibility_report.txt
│
├── src/
│   └── feasibility_check.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Install

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python src/feasibility_check.py
```

---

## Output

```
outputs/
└── ml_feasibility_report.txt
```

---

## Conclusion

The program inspects the dataset and recommends whether Classification, Regression, or Clustering is the most suitable machine learning approach.