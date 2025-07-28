import pandas as pd

# Load the Excel file
df = pd.read_csv("PeMS08_rel.csv") 

# Keep only the desired columns
df = df[['origin_id', 'destination_id', 'cost']]

# Save the updated DataFrame to a new CSV file
df.to_csv('matris_mojaverat_fazayi.csv', index=False)  