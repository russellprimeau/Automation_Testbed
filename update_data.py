import pandas as pd

def read_last_lines(filename, num_lines):
  """
  This function reads and prints the last `num_lines` from a CSV file.

  Args:
      filename: The path to the CSV file.
      num_lines: The number of lines to read from the end of the file.
  """
  with open(filename, 'r') as f:
    lines = f.readlines()
    last_lines = lines[-num_lines:]  # Get lines from the end using slicing
    for line in last_lines:
      print(line.rstrip())  # Print lines with trailing newline removed

# Create a sample DataFrame (replace with your actual data)
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)

print(df)

# Append the DataFrame to an existing CSV (without headers)
df.to_csv('online_pfl_data.csv', mode='a', index=False, header=False)
print("Dataframe appended to online_pfl_data.csv:")

read_last_lines('online_pfl_data', 3)
