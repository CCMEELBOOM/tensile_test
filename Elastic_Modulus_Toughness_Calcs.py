import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("tensile_testing_values.csv")
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()


#print(df.columns) #good for checking column names

steel_1_strain = df["Steel1_Strain"]
steel_1_stress = df["Steel1_Stress"]
steel_2_strain = df["Steel2_Strain"]
steel_2_stress = df["Steel2_Stress"]

#Isolates elastic region data for steel 1 and steel 2, which will be used to calculate the elastic modulus
steel_1_strain_elastic = steel_1_strain[0:572] 
steel_1_stress_elastic = steel_1_stress[0:572] 
steel_2_strain_elastic = steel_2_strain[0:433]
steel_2_stress_elastic = steel_2_stress[0:433]

aluminum_1_strain = df["Aluminum1_Strain"]
aluminum_1_stress = df["Aluminum1_Stress"]
aluminum_2_strain = df["Aluminum2_Strain"]
aluminum_2_stress = df["Aluminum2_Stress"]

#Isolates elastic region data for aluminum 1 and aluminum 2, which will be used to calculate the elastic modulus
aluminum_1_strain_elastic = aluminum_1_strain[0:837]
aluminum_1_stress_elastic = aluminum_1_stress[0:837]
aluminum_2_strain_elastic = aluminum_2_strain[0:1006]
aluminum_2_stress_elastic = aluminum_2_stress[0:1006]

# Finds the slope of the elastic region for steel 1 and steel 2, which is the elastic modulus, using np.polyfit to fit a line to the elastic region data
elastic_modulus_steel_1 = np.polyfit(steel_1_strain_elastic, steel_1_stress_elastic, 1) # This will give us the elastic modulus for steel 1
 
elastic_modulus_steel_2 = np.polyfit(steel_2_strain_elastic, steel_2_stress_elastic, 1) # This will give us the elastic modulus for steel 2

elastic_modulus_steel = (elastic_modulus_steel_1[0] + elastic_modulus_steel_2[0]) / 2 # This will give us the average elastic modulus for steel

print(f"Elastic Modulus - Steel: {elastic_modulus_steel} MPa")

#Finds the slope of the elastic region for aluminum 1 and aluminum 2, which is the elastic modulus, using np.polyfit to fit a line to the elastic region data
elastic_modulus_aluminum_1 = np.polyfit(aluminum_1_strain_elastic, aluminum_1_stress_elastic, 1) # This will give us the elastic modulus for aluminum 1

elastic_modulus_aluminum_2 = np.polyfit(aluminum_2_strain_elastic, aluminum_2_stress_elastic, 1) # This will give us the elastic modulus for aluminum 2

elastic_modulus_aluminum = (elastic_modulus_aluminum_1[0] + elastic_modulus_aluminum_2[0]) / 2 # This will give us the average elastic modulus for aluminum

print(f"Elastic Modulus - Aluminum: {elastic_modulus_aluminum} MPa")

toughness_steel_1 = np.trapezoid(steel_1_stress, steel_1_strain) # This will give us the toughness for steel 1 by calculating the area under the stress-strain curve using the trapezoidal rule
toughness_steel_2 = np.trapezoid(steel_2_stress, steel_2_strain) # This will give us the toughness for steel 2 by calculating the area under the stress-strain curve using the trapezoidal rule
toughness_steel = (toughness_steel_1 + toughness_steel_2) / 2 # This will give us the average toughness for steel
print(f"Toughness - Steel: {toughness_steel} MJ/m^3")

toughness_aluminum_1 = np.trapezoid(aluminum_1_stress, aluminum_1_strain) # This will give us the toughness for aluminum 1 by calculating the area under the stress-strain curve using the trapezoidal rule
toughness_aluminum_2 = np.trapezoid(aluminum_2_stress, aluminum_2_strain) # This will give us the toughness for aluminum 2 by calculating the area under the stress-strain curve using the trapezoidal rule
toughness_aluminum = (toughness_aluminum_1 + toughness_aluminum_2) / 2 # This will give us the average toughness for aluminum
print(f"Toughness - Aluminum: {toughness_aluminum} MJ/m^3")
