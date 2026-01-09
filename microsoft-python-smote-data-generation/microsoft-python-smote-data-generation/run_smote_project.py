import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score,
    classification_report,
    roc_curve
)
from imblearn.over_sampling import SMOTE


def main():
    # ========== LOAD DATA ==========
    print("Loading dataset from 'diabetes.csv' ...")
    df = pd.read_csv("diabetes.csv")
    print("Dataset loaded. Shape:", df.shape)

    # Optional: show class distribution
    print("\nOriginal class distribution:")
    print(df["Outcome"].value_counts())

    # ========== SPLIT ==========
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    x_train, x_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # ========== SCALE ==========
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    # ========== APPLY SMOTE ==========
    print("\nApplying SMOTE to training data ...")
    sm = SMOTE(random_state=42)
    x_train_smote, y_train_smote = sm.fit_resample(x_train_scaled, y_train)

    print("Class distribution after SMOTE:")
    print(y_train_smote.value_counts())

    # ========== MODELS ==========
    model_original = LogisticRegression(solver="liblinear", max_iter=200)
    model_smote = LogisticRegression(solver="liblinear", max_iter=200)

    # ========== TRAIN ==========
    print("\nTraining models ...")
    model_original.fit(x_train_scaled, y_train)
    model_smote.fit(x_train_smote, y_train_smote)

    # ========== PREDICTIONS ==========
    print("\nPredicting on test data ...")
    y_pred_original = model_original.predict(x_test_scaled)
    y_pred_prob_original = model_original.predict_proba(x_test_scaled)[:, 1]

    y_pred_smote = model_smote.predict(x_test_scaled)
    y_pred_prob_smote = model_smote.predict_proba(x_test_scaled)[:, 1]

    # ========== EVALUATION FUNCTION ==========
    def evaluate(name, y_true, y_pred, y_prob):
        print(f"\n===== {name} =====")
        print("Accuracy :", accuracy_score(y_true, y_pred))
        print("Precision:", precision_score(y_true, y_pred))
        print("Recall   :", recall_score(y_true, y_pred))
        print("ROC-AUC  :", roc_auc_score(y_true, y_prob))
        print("\nClassification Report:\n", classification_report(y_true, y_pred))

    # ========== EVALUATE BOTH MODELS ==========
    evaluate("Original Model (Imbalanced)", y_test, y_pred_original, y_pred_prob_original)
    evaluate("SMOTE Model (Balanced)", y_test, y_pred_smote, y_pred_prob_smote)

    # ========== ROC CURVE ==========
    print("\nSaving ROC curve plot as 'roc_curve.png' ...")

    fpr_org, tpr_org, _ = roc_curve(y_test, y_pred_prob_original)
    fpr_sm, tpr_sm, _ = roc_curve(y_test, y_pred_prob_smote)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr_org, tpr_org, label="Original Model")
    plt.plot(fpr_sm, tpr_sm, label="SMOTE Model")
    plt.plot([0, 1], [0, 1], linestyle='--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison")
    plt.legend()
    plt.tight_layout()
    plt.savefig("roc_curve.png")

    print("ROC curve saved as 'roc_curve.png'")
    print("\n===== SCRIPT FINISHED SUCCESSFULLY =====")


if __name__ == "__main__":
    main()
