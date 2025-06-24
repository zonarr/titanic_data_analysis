import pandas as pd
def describe_data(df:pd.DataFrame)-> None:
    print("The first 5 rows are:")
    print(df.head())
    print("The last 5 rows are:")
    print(df.tail())
    print(f"The dimensions are {df.shape}")
    print("The summaries are:")
    df.info()
    print("The description of the data is:")
    df.describe()
