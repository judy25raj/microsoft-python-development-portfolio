# ⚖️ Synthetic Data Generation with SMOTE

**Imbalanced Learning • Machine Learning Preprocessing • Model Evaluation • Python**

## 🧠 Overview
This project demonstrates how to address class imbalance in real-world datasets using **SMOTE (Synthetic Minority Over-sampling Technique)**.

It implements a complete preprocessing and evaluation pipeline to:
- Balance skewed classes
- Train and compare models
- Measure performance improvements using ROC and classification metrics

The workflow reflects production-style data science practices where data quality and class balance directly impact model reliability.

## 🎯 Capabilities Demonstrated
- Class imbalance detection and analysis  
- Synthetic data generation using SMOTE  
- Train/test splitting and model evaluation  
- ROC curve visualization and performance comparison  
- Reproducible ML experimentation workflow  

## 📂 Project Structure
microsoft-python-smote-data-generation/
├── Project_Synthetic_Data_Generation_Clean.ipynb
├── Project_Synthetic_Data_Generation_Teaching.ipynb
├── run_smote_project.py
├── diabetes.csv
├── roc_curve.png
├── requirements.txt
└── README.md

## ⚙️ How to Run
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
python run_smote_project.py

## 📊 Output
The pipeline trains models before and after SMOTE and generates ROC curves.

## 🧠 Engineering Value
Improves minority class recall and ensures fair model evaluation.

## 🛠 Technologies
Python, Pandas, Scikit-learn, imbalanced-learn, Matplotlib

## 🧩 Use Cases
Fraud detection, Medical diagnosis, Churn modeling, Risk scoring
