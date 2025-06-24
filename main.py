import pandas as pd
import da

def main():
    df = pd.read_csv("train.csv")
    da.describe_data(df)
    age = df["Age"]
    age_fare = df["Age","Fare"]
    age_sorted = age.sort_values()

if __name__ == "__main__":
	main()
