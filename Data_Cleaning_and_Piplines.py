import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv(r"C:\Users\Admin\PROJECTS\AI_Projects\Data_Handling\Data\dirty_cafe_sales.csv"))
df.info()
print(" ")

#finding the null values in the dataset
print(df.isnull().sum(), "\n")

#handling the null values
df["Item"] = df["Item"].fillna(df["Item"].mode()[0])
df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce').fillna(df["Quantity"].mode()[0])
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors='coerce').fillna(df["Price Per Unit"].mode()[0])
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors='coerce').fillna(df["Total Spent"].mode()[0])
df["Payment Method"] = df["Payment Method"].fillna(df["Payment Method"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Transaction Date"] = df["Transaction Date"].fillna(df["Transaction Date"].mode()[0])


# Replace "UNKNOWN" and "ERROR" with mode/mean values
df["Item"] = df["Item"].replace(["UNKNOWN", "ERROR"], df["Item"].mode()[0])
df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce').replace(["UNKNOWN", "ERROR"], pd.to_numeric(df["Quantity"], errors='coerce').mean())
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors='coerce').replace(["UNKNOWN", "ERROR"], pd.to_numeric(df["Price Per Unit"], errors='coerce').mean())
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors='coerce').replace(["UNKNOWN", "ERROR"], pd.to_numeric(df["Total Spent"], errors='coerce').mean())
df["Payment Method"] = df["Payment Method"].replace(["UNKNOWN", "ERROR"], df["Payment Method"].mode()[0])
df["Location"] = df["Location"].replace(["UNKNOWN", "ERROR"], df["Location"].mode()[0])
df["Transaction Date"] = df["Transaction Date"].replace(["UNKNOWN", "ERROR"], df["Transaction Date"].mode()[0])

print(df.head(20))
print(" ")

#writing the cleaned data to a new csv file
df.to_csv(r"C:\Users\Admin\PROJECTS\AI_Projects\Data_Handling\Data\Cleaned_Cafe_Sales_Data.csv", index=False)