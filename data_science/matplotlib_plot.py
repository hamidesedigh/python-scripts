"""
matplotlib_plot.py
------------------
Comprehensive introduction to Matplotlib plotting.
Based on:
- MyLearningNotes.xlsx (Visualization sheet)
- DataCamp "Matplotlib" and "Python for Data Science" cheat sheets

Covers:
1. Basic Plotting
2. Customizing Plots (Titles, Labels, Legends, Grid)
3. Multiple Plots and Subplots
4. Styles, Colors, and Markers
5. Annotations and Text
6. Common Plot Types (Line, Scatter, Bar, Histogram, Boxplot)
7. Saving and Clearing Figures

⚙️ This script was AI-assisted, generated and refined with the help of ChatGPT to accelerate learning and documentation.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate sample data
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

# ===============================================================
# 1. Basic Plotting
# ===============================================================
print("\n=== 1. Basic Plotting ===")

plt.figure(figsize=(8, 4))
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title("Basic Line Plot: sin(x) & cos(x)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# ===============================================================
# 2. Customizing Plots
# ===============================================================
print("\n=== 2. Customizing Plots ===")

plt.figure(figsize=(8, 4))
plt.plot(x, y1, color='teal', linestyle='--', linewidth=2, marker='o', label='sin(x)')
plt.plot(x, y2, color='orange', linestyle='-', linewidth=2, marker='s', label='cos(x)')

plt.title("Customized Plot Example", fontsize=14, fontweight='bold')
plt.xlabel("Angle (radians)")
plt.ylabel("Function value")
plt.legend(loc='best')
plt.grid(alpha=0.4)
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.show()

# ===============================================================
# 3. Multiple Plots and Subplots
# ===============================================================
print("\n=== 3. Multiple Plots and Subplots ===")

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
axes[0, 0].plot(x, y1, 'r--', label='sin(x)')
axes[0, 1].plot(x, y2, 'b-', label='cos(x)')
axes[1, 0].scatter(x, y1, color='green', label='sin(x) points')
axes[1, 1].bar(np.arange(5), np.random.randint(1, 10, 5), color='skyblue', label='Random Bar')

for ax in axes.flat:
    ax.legend()
    ax.grid(True)

fig.suptitle("Multiple Subplots Example", fontsize=16)
plt.tight_layout()
plt.show()

# ===============================================================
# 4. Styles, Colors, and Markers
# ===============================================================
print("\n=== 4. Styles, Colors, and Markers ===")

plt.figure(figsize=(8, 4))
plt.style.use('seaborn-v0_8-muted')

plt.plot(x, np.sin(x), 'o--', color='crimson', label='sin(x)')
plt.plot(x, np.sin(x + 1), 's-', color='navy', label='sin(x + 1)')
plt.plot(x, np.sin(x + 2), 'd-.', color='darkgreen', label='sin(x + 2)')

plt.title("Line Styles and Markers")
plt.xlabel("X-axis")
plt.ylabel("sin(x) Variations")
plt.legend()
plt.show()

# ===============================================================
# 5. Annotations and Text
# ===============================================================
print("\n=== 5. Annotations and Text ===")

plt.figure(figsize=(8, 4))
plt.plot(x, y1, label='sin(x)', color='purple')
plt.title("Plot with Annotation")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.legend()

# Annotate a specific point
x_point = np.pi / 2
y_point = np.sin(x_point)
plt.scatter(x_point, y_point, color='red')
plt.annotate("Peak (π/2, 1)", xy=(x_point, y_point),
             xytext=(x_point + 1, y_point - 0.2),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.text(6, 0, "y = sin(x)", fontsize=12, style='italic')
plt.show()

# ===============================================================
# 6. Common Plot Types
# ===============================================================
print("\n=== 6. Common Plot Types ===")

# Bar Plot
data = {'A': 23, 'B': 45, 'C': 56, 'D': 78}
plt.figure(figsize=(6, 4))
plt.bar(data.keys(), data.values(), color='steelblue')
plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# Histogram
plt.figure(figsize=(6, 4))
data_hist = np.random.randn(1000)
plt.hist(data_hist, bins=30, color='salmon', edgecolor='black', alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure(figsize=(6, 4))
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data_box, vert=True, patch_artist=True)
plt.title("Boxplot Example")
plt.xticks([1, 2, 3], ['std=1', 'std=2', 'std=3'])
plt.show()

# Scatter Plot with color & size mapping
plt.figure(figsize=(6, 4))
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = 500 * np.random.rand(N)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.title("Scatter Plot with Color & Size")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label='Color scale')
plt.show()

# ===============================================================
# 7. Saving and Clearing Figures
# ===============================================================
print("\n=== 7. Saving and Clearing Figures ===")

plt.figure(figsize=(8, 4))
plt.plot(np.arange(10), np.random.randn(10), marker='o')
plt.title("Saving Figure Example")
plt.xlabel("Index")
plt.ylabel("Random Value")
plt.grid(True)

# Save as PNG and PDF
plt.savefig("example_plot.png", dpi=150)
plt.savefig("example_plot.pdf", dpi=150, transparent=True)
print("Figures saved as 'example_plot.png' and 'example_plot.pdf'")

# Clear and close
plt.cla()  # clear axis
plt.clf()  # clear figure
plt.close()

print("\n✅ matplotlib_plot.py executed successfully!")
