import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv(r'C:\Users\Admin\PROJECTS\AI_Projects\Data_Handling\Data\epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")

    # Create first line of best fit (all data)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.intercept + res.slope * x_pred
    ax.plot(x_pred, y_pred, 'r', label="Best fit (1880-2014)")

    # Create second line of best fit (from 2000 onward)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    ax.plot(x_recent, y_recent, 'g', label="Best fit (2000-2014)")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    # Save image and return fig
    fig.savefig("sea_level_plot.png")
    return fig

draw_plot()
plt.show()