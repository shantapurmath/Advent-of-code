import pandas as pd
# Read the input text file into a DataFrame with space as the delimiter
input_file_path = 'dminput1212.txt'
output_file_path = 'output_file_DM1.txt'

df = pd.read_csv(input_file_path, delimiter=' ', skipinitialspace=True)
#df = pd.read_csv(input_file_path)
print(df.columns)
print(df)

# Define the desired length for each column
customer_no_length = 10
branch_length = 6
account_length = 8
relation_type_length = 3

# Conditionally add leading zeros or spaces based on the length of each column
df['CUSTOMER_NO'] = df['CUSTOMER_NO'].apply(lambda x: str(x).zfill(customer_no_length) if len(str(x)) != customer_no_length else x)
df['BRANCH_NO'] = df['BRANCH_NO'].apply(lambda x: str(x).zfill(branch_length) if len(str(x)) != branch_length else x)
df['ACCOUNT_NO'] = df['ACCOUNT_NO'].apply(lambda x: str(x).zfill(account_length) if len(str(x)) != account_length else x)
df['RELATION_TYPE'] = df['RELATION_TYPE'].apply(lambda x: str(x).ljust(relation_type_length) if len(str(x)) != relation_type_length else x)
# Save the modified DataFrame to a new text file

df.to_csv(output_file_path, sep=' ', index=False, header=False)
print(f"Processed data saved to {output_file_path}")

# Replace 'your_input_file.txt' and 'your_output_file.txt' with your actual file names
input_file = 'output_file_DM1.txt'
output_file = 'intermidiateout.txt'

with open(input_file, 'r') as file:
    lines = file.readlines()

# Filter lines that start with a number and remove spaces
filtered_lines = [line.strip().replace(" ", "") for line in lines if
                  line.strip().startswith(('0','1', '2', '3', '4', '5', '6', '7', '8', '9'))]

# Combine lines with the same key
combined_lines = {}
for line in filtered_lines:
    key = line[:10]  # Assuming the key is the first 10 characters
    content = line[10:]  # Content after the key
    combined_lines.setdefault(key, []).append(content)

# Create a DataFrame with the combined lines
df = pd.DataFrame(
    {'key': list(combined_lines.keys()), 'content': [' '.join(contents) for contents in combined_lines.values()]})

# Store the result in a new file
df.to_csv(output_file, index=False, header=False)

# Read lines from the file
file_path = 'intermidiateout.txt'  # Replace 'your_file.txt' with the actual path to your file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove spaces and replace commas
modified_lines = [line.replace(' ', '').replace(',', 'TCWCUSAC ') for line in lines]

# Write the modified lines back to the file
output_file_path = 'DMTOOLFINAL_OUT.txt'  # Replace 'output.txt' with the desired output file path
with open(output_file_path, 'w') as output_file:
    output_file.writelines(modified_lines)
