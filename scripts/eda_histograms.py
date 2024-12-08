import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)


# Select columns of interest
variables = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']

# Histogram Plotting 

# Define a function to plot histograms
def plot_histograms(data, variables, bins=30, output_path="../output/histograms.png"):
    """
    Plots histograms for the specified variables in the dataset.

    Parameters:
    - data: DataFrame containing the data
    - variables: List of column names to plot
    - bins: Number of bins for the histograms
    - output_path: Path to save the final figure
    """
    num_vars = len(variables)
    rows = (num_vars + 2) // 3  # Calculate rows for a grid layout
    cols = 3  # Fixed columns for layout

    plt.figure(figsize=(15, 5 * rows))

    for i, var in enumerate(variables, 1):
        plt.subplot(rows, cols, i)
        sns.histplot(data[var], kde=True, bins=bins, color='blue', alpha=0.6)
        plt.title(f"Distribution of {var}", fontsize=12)
        plt.xlabel(var)
        plt.ylabel("Frequency")
        plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()

# Plot histograms for the selected variables
plot_histograms(df, variables)
