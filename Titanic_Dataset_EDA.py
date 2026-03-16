import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# Load the Titanic dataset
df = pd.read_csv(r".\Data\titanic.csv")
print(df.head(20))
df.info()
df.describe()