
import pandas as pd

def load(path):
    return pd.read_csv(path)

def analyze(df):
    out = []
    out.append(f"Shape: {df.shape}")
    out.append("\nColumn Types:")
    out.append(str(df.dtypes))
    out.append("\nHead:")
    out.append(str(df.head()))
    out.append("\nDescribe:")
    out.append(str(df.describe()))
    out.append("\nGender Distribution:")
    out.append(str(df['gender'].value_counts()))
    top5 = df.sort_values('total_spend', ascending=False)[['customer_id','first_name','last_name','total_spend']]
    out.append("\nTop 5 Customers:")
    out.append(str(top5.head()))
    return "\n".join(out)

def main():
    df = load("data/customer_data_50.csv")
    summary = analyze(df)
    with open("results/summary.txt","w") as f:
        f.write(summary)
    print("Done. See results/summary.txt")

if __name__ == "__main__":
    main()
