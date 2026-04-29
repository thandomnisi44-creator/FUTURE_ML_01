import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# Prompt the user to upload the 'Sample - Superstore.csv' file
print("Please upload the 'Sample - Superstore.csv' file.")
uploaded = files.upload()

# Get the actual name of the uploaded file
file_name = ''
for fn in uploaded.keys():
    file_name = fn
    break # Assuming only one file is uploaded

# Load the dataset using the actual uploaded file name
df = pd.read_csv(file_name, encoding='latin1')

# Ensure 'Order Date' is in datetime format and aggregate daily sales
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Aggregate Sales by Order Date
daily_sales = df.groupby('Order Date')['Sales'].sum().reset_index()
daily_sales.columns = ['date', 'sales']

# Sort by date
daily_sales = daily_sales.sort_values('date').reset_index(drop=True)

# Plot the time series of daily sales
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['date'], daily_sales['sales'], color='royalblue', linewidth=1.5)
plt.title('Daily Sales Over Time', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()