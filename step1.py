import pandas as pd

df1 = pd.read_csv(r"C:\Users\AnjaliGopika\Downloads\AzurePipelinecopy copy\AzurePipelinecopy copy\DATA_INPUT_MAY_INTERGROW\Secondary Order Dump (New)_01-03-2025 00_00_00 to 31-03-2025 00_00_00_17443478832209649340464-d166-4bc7-a51e-84f1e2c0fc14 (1).csv")
df2 = pd.read_excel(r"C:\Users\AnjaliGopika\Downloads\AzurePipelinecopy copy\AzurePipelinecopy copy\DATA_INPUT_MAY_INTERGROW\data cleaned stanish.xlsx")
print("Succesfully read the file and saved as df")