import pandas as pd

# Create a sample DataFrame (replace with your actual data)
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)

print(df)

# Append the DataFrame to an existing CSV (without headers)
df.to_csv('online_pfl_data.csv', mode='a', index=False, header=False)
print("Dataframe appended to online_pfl_data.csv")
