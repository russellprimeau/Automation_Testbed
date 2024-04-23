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

def commit_changes(data_file, commit_message):
  """
  Stages and commits changes to the data file using Git commands.

  Args:
      data_file (str): Path to the data file.
      commit_message (str): Message describing the commit.
  """
  !git add data_file
  !git commit -m "{commit_message}"

# Create a sample DataFrame (replace with your actual data)
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)

# Append the DataFrame to an existing CSV (without headers)
data_file = "online_pfl_data.csv"
df.to_csv(data_file, mode='a', index=False, header=False)
print("Dataframe appended to ", data_file)

commit_changes(data_file, "Appended new data to CSV file")
read_last_lines(data_file, 6)
