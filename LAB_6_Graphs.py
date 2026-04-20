import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("tensile_testing_values.csv")

#print(df.columns) #good for checking column names

steel_1_strain = df["Steel1_Strain"]
steel_1_stress = df["Steel1_Stress"]
steel_2_strain = df["Steel2_Strain"]
steel_2_stress = df["Steel2_Stress"]

aluminum_1_strain = df["Aluminum1_Strain"]
aluminum_1_stress = df["Aluminum1_Stress"]
aluminum_2_strain = df["Aluminum2_Strain"]
aluminum_2_stress = df["Aluminum2_Stress"]

steel_1_elastic_strain = steel_1_strain[0:650] # First 700 data points are in the elastic region, so we #print(len(steel_1_elastic_strain)) # Check the length of the elastic strain data to ensure it is correct
steel_1_elastic_stress = steel_1_stress[0:650]
steel_2_elastic_strain = steel_2_strain[0:600]
steel_2_elastic_stress = steel_2_stress[0:600]
# First 1253 data points are in the elastic region for aluminum, so we use that range for aluminum 1 and aluminum 2
aluminum_1_elastic_strain = aluminum_1_strain[0:1000]
aluminum_1_elastic_stress = aluminum_1_stress[0:1000]
aluminum_2_elastic_strain = aluminum_2_strain[0:1150]
aluminum_2_elastic_stress = aluminum_2_stress[0:1150]

# Plot of Steel 1 and Aluminum 1
plt.figure(figsize=(10, 6))

plt.plot(steel_1_strain, steel_1_stress,
         label="Steel 1",
         color="#FF8C00",
         linewidth=1.8)
plt.plot(aluminum_1_strain, aluminum_1_stress,
         label="Aluminum 1",
         color="#4682B4",
         linewidth=1.8)

plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Steel 1 vs Aluminum 1", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.55, y=np.arange(0, 451, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot of Steel 2 and Aluminum 2
plt.figure(figsize=(10, 6))

plt.plot(steel_2_strain, steel_2_stress,
        label="Steel 2",   
        color="#FFAE17",
         linewidth=1.8)
plt.plot(aluminum_2_strain, aluminum_2_stress,
        label="Aluminum 2", 
        color="#4D6175",
         linewidth=1.8) 
plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Steel 2 vs Aluminum 2", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.55, y=np.arange(0, 451, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot of Steel 1 and Steel 2
plt.figure(figsize=(10, 6))

plt.plot(steel_1_strain, steel_1_stress,
         label="Steel 1",
            color="#FF8C00",
            linewidth=1.8)
plt.plot(steel_2_strain, steel_2_stress,
         label="Steel 2",   
            color="#FFAE17",
            linewidth=1.8)
plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Steel 1 vs Steel 2", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.55, y=np.arange(0, 401, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot of Aluminum 1 and Aluminum 2
plt.figure(figsize=(10, 6))

plt.plot(aluminum_1_strain, aluminum_1_stress,
            label="Aluminum 1",
                color="#4682B4",
                linewidth=1.8)
plt.plot(aluminum_2_strain, aluminum_2_stress,
            label="Aluminum 2",
                color="#4D6175",
                linewidth=1.8)
plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Aluminum 1 vs Aluminum 2", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.2, y=np.arange(0, 451, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot elastic region Steel 1 and Steel 2
plt.figure(figsize=(10, 6))

plt.plot(steel_1_elastic_strain, steel_1_elastic_stress,
         label="Steel 1",
            color="#FF8C00",
            linewidth=1.8)
plt.plot(steel_2_elastic_strain, steel_2_elastic_stress,
            label="Steel 2",   
                color="#FFAE17",
                linewidth=1.8)
plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Steel 1 vs Steel 2 (Elastic Region)", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.0012, y=np.arange(0, 181, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot elastic region Aluminum 1 and Aluminum 2
plt.figure(figsize=(10, 6))

plt.plot(aluminum_1_elastic_strain, aluminum_1_elastic_stress,
            label="Aluminum 1",
                color="#4682B4",
                linewidth=1.8)
plt.plot(aluminum_2_elastic_strain, aluminum_2_elastic_stress,
            label="Aluminum 2",
                color="#4D6175",
                linewidth=1.8)
plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Aluminum 1 vs Aluminum 2 (Elastic Region)", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.0055, y=np.arange(0, 326, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot elastic region Aluminum 1 and Steel 1
plt.figure(figsize=(10, 6))

plt.plot(aluminum_1_elastic_strain, aluminum_1_elastic_stress,
            label="Aluminum 1",
                color="#4682B4",
                linewidth=1.8)
plt.plot(steel_1_elastic_strain, steel_1_elastic_stress,
            label="Steel 1",
                color="#FF8C00",
                linewidth=1.8)
plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Aluminum 1 vs Steel 1 (Elastic Region)", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.0055, y=np.arange(0, 326, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()

# Plot elastic region Aluminum 2 and Steel 2
plt.figure(figsize=(10, 6))

plt.plot(aluminum_2_elastic_strain, aluminum_2_elastic_stress,
            label="Aluminum 2",
                color="#4D6175",
                linewidth=1.8)
plt.plot(steel_2_elastic_strain, steel_2_elastic_stress,
            label="Steel 2",
                color="#FFAE17",
                linewidth=1.8)
plt.xlabel("Strain (mm/mm)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.ylabel("Stress (MPa)", fontname="Times New Roman", fontsize=12, fontweight="bold")
plt.title("Stress-Strain Curves: Aluminum 2 vs Steel 2 (Elastic Region)", fontname="Times New Roman", fontsize=14, fontweight="bold")
plt.hlines(xmin=0, xmax=.0055, y=np.arange(0, 326, 40), colors="black", linewidth=.75, zorder=0)
plt.legend()
plt.tight_layout()
plt.show()