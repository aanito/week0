import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

# Select relevant columns
variables = ['GHI', 'Tamb', 'WS', 'RH', 'BP']
df = df[variables].dropna()  # Remove rows with missing values

# -------------------- Bubble Chart --------------------

# Define a function to create bubble charts
def plot_bubble_chart(df, x, y, size, color=None, title="", output_path="../output/bubble_chart.png"):
    """
    Creates a bubble chart to explore complex relationships between variables.

    Parameters:
    - df: DataFrame containing the data
    - x: Column name for x-axis
    - y: Column name for y-axis
    - size: Column name for bubble size
    - color: Column name for bubble color (optional)
    - title: Title of the plot
    - output_path: Path to save the plot
    """
    plt.figure(figsize=(10, 6))

    # Normalize the size variable for better bubble scaling
    size_scaled = (df[size] - df[size].min()) / (df[size].max() - df[size].min()) * 100 + 10

    # Create bubble chart
    scatter = plt.scatter(
        df[x],
        df[y],
        s=size_scaled,  # Bubble size
        c=df[color] if color else None,  # Bubble color
        cmap='viridis' if color else None,
        alpha=0.7,
        edgecolors='w'
    )

    # Add color bar if color is used
    if color:
        plt.colorbar(scatter, label=color)

    # Plot settings
    plt.title(title, fontsize=14)
    plt.xlabel(x, fontsize=12)
    plt.ylabel(y, fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()

    # Save and show plot
    plt.savefig(output_path)
    plt.show()

# Plot GHI vs. Tamb with bubble size as WS and color as RH
plot_bubble_chart(
    df,
    x='GHI',
    y='Tamb',
    size='WS',
    color='RH',
    title="Bubble Chart: GHI vs. Tamb (Bubble Size: WS, Color: RH)",
    output_path="../output/bubble_chart_ghi_tamb_ws_rh.png"
)

# Plot GHI vs. Tamb with bubble size as BP (Barometric Pressure)
plot_bubble_chart(
    df,
    x='GHI',
    y='Tamb',
    size='BP',
    title="Bubble Chart: GHI vs. Tamb (Bubble Size: BP)",
    output_path="../output/bubble_chart_ghi_tamb_bp.png"
)
