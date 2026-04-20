import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("force_displacement_values.csv")

print(df.columns) #good for checking column names

steel1_force = df["Steel1_Force"]
steel1_displacement = df["Steel1_Displacement "]
steel2_force = df["Steel2_Force"]
steel2_displacement = df["Steel2_Displacement"]
aluminum1_force = df["Aluminum1_Force"]
aluminum1_displacement = df["Aluminum1_Displacement"]
aluminum2_force = df["Aluminum2_Force"]
aluminum2_displacement = df["Aluminum2_Displacement"]

# Plot of Steel 1 and Aluminum 1
plt.figure(figsize=(10, 6))

plt.plot(steel1_displacement, steel1_force,
         label="Steel 1",
         color="#FF8C00",
         linewidth=1.8)
plt.plot(aluminum1_displacement, aluminum1_force,
         label="Aluminum 1",
         color="#4682B4",
         linewidth=1.8)

plt.xlabel("Displacement (mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Force (kN)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Force-Displacement Curves: Steel 1 vs Aluminum 1", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=19, y=np.arange(0, 7, 1), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot of Steel 2 and Aluminum 2
plt.figure(figsize=(10, 6))

plt.plot(steel2_displacement, steel2_force,
         label="Steel 2",
         color="#FFAE17",
         linewidth=1.8)
plt.plot(aluminum2_displacement, aluminum2_force,
         label="Aluminum 2",
         color="#4D6175",
         linewidth=1.8)

plt.xlabel("Displacement (mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Force (kN)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Force-Displacement Curves: Steel 2 vs Aluminum 2", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=19, y=np.arange(0, 7, 1), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot of Steel 1 and Steel 2
plt.figure(figsize=(10, 6))

plt.plot(steel1_displacement, steel1_force,
         label="Steel 1",
         color="#FF8C00",
         linewidth=1.8)
plt.plot(steel2_displacement, steel2_force,
         label="Steel 2",
         color="#FFAE17",
         linewidth=1.8)

plt.xlabel("Displacement (mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Force (kN)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Force-Displacement Curves: Steel 1 vs Steel 2", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=19, y=np.arange(0, 7, 1), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot of Aluminum 1 and Aluminum 2
plt.figure(figsize=(10, 6))

plt.plot(aluminum1_displacement, aluminum1_force,
         label="Aluminum 1",
         color="#4682B4",
         linewidth=1.8)
plt.plot(aluminum2_displacement, aluminum2_force,
         label="Aluminum 2",
         color="#4D6175",
         linewidth=1.8)

plt.xlabel("Displacement (mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Force (kN)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Force-Displacement Curves: Aluminum 1 vs Aluminum 2", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=7.5, y=np.arange(0, 7, 1), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()