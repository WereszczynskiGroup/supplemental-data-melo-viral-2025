import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter


plt.rcParams['font.family'] = 'Arial',
plt.rcParams['font.size'] = 10

# Define datasets and which sum type they use
datasets = [
    ("virus_widom", "Sum"),
    ("virus_alpha", "Sum2"),
    ("trunc_euk_widom", "Sum2"),
    ("trunc_euk_alpha", "Sum2"),
    ("euk_widom", "Sum"),
    ("euk_alpha", "Sum"),
]

# Descriptive biological titles for plotting
title_map = {
    "virus_widom": "Viral / Widom 601 DNA",
    "virus_alpha": "Viral / Alpha-Satellite DNA",
    "trunc_euk_widom": "Truncated Euk. / Widom 601 DNA",
    "trunc_euk_alpha": "Truncated Euk. / Alpha-Satellite DNA",
    "euk_widom": "Eukaryotic / Widom 601 DNA",
    "euk_alpha": "Eukaryotic / Alpha-Satellite DNA"
}

file_suffixes = [
    "_combined_rmsd_con3_1.csv",
    "_combined_rmsd_con3_2.csv",
    "_combined_rmsd_con3_3.csv",
    "_combined_rmsd_con3_4.csv"
]

fig, axs = plt.subplots(3, 2, figsize=(5.5, 5), sharex=True, sharey=True, gridspec_kw={'wspace': 0.2, 'hspace': 0.35})
axs = axs.flatten()

for plot_idx, (prefix, sum_column_type) in enumerate(datasets):
    all_runs = []

    for suffix in file_suffixes:
        filename = f"{prefix}{suffix}"
        df = pd.read_csv(filename)

        # For files needing to calculate Sum
        if sum_column_type == "Sum":
            df = df.set_index("Frame")
            df["Sum"] = df.sum(axis=1)
            series = df["Sum"]
        else:
            # Use Sum2 column
            if "Frame" in df.columns:
                df = df.set_index("Frame")
            series = df["Sum2"]

        # Apply Savitzky-Golay filter
        smoothed = savgol_filter(series, 100, 1)
        all_runs.append(smoothed)
        x_vals = series.index / 10

    # Plot each run
    ax = axs[plot_idx]

    colors = ["#0072B2", "#D55E00", "#009E73", "#CC79A7"]
    for i, run in enumerate(all_runs):
        ax.plot(x_vals/1000, run, label=f"Run {i+1}", color=colors[i], linewidth=1.0, alpha=0.9)


    # Format subplot
    ax.set_title(title_map[prefix], fontsize=10)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 60)
    if plot_idx % 2 == 0:
        ax.set_ylabel("# BP Unwrapped", fontsize=10)
    if plot_idx >= 4:
        ax.set_xlabel("Time (µs)", fontsize=10)
    ax.tick_params(labelsize=10)

# Format the full figure
fig.suptitle("Total DNA Unwrapping – All Systems", fontsize=12, weight='bold')
axs[5].legend(loc="upper right", fontsize=9)

plt.savefig("FigS2-Total_DNA_Unwrap.pdf")

