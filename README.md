# Daily Sales Visualization

This script loads sales data from a CSV file, preprocesses it to aggregate daily sales, and then visualizes the daily sales trend over time using a line plot.

## Features

*   **Data Loading**: Prompts the user to upload a CSV file containing sales data.
*   **Date Conversion**: Converts the 'Order Date' column to datetime objects.
*   **Daily Aggregation**: Aggregates sales data to calculate total daily sales.
*   **Time Series Plotting**: Generates a line plot to visualize the daily sales trend.

## Dependencies

This script requires the following Python libraries:

*   `pandas`
*   `matplotlib`

## How to Use

1.  **Upload Data**: When prompted, upload your `Sample - Superstore.csv` file. This file should contain an 'Order Date' column and a 'Sales' column.
2.  **Run the Cell**: Execute the code cell containing the script.
3.  **Review Plot**: The script will display a line plot showing daily sales over time.

## Input Data Format

The CSV file (e.g., `Sample - Superstore.csv`) should contain at least two columns:

*   `Order Date`: The date of the order (e.g., 'YYYY-MM-DD').
*   `Sales`: The sales amount for the order.

## Output

The script generates:

*   A line plot titled 'Daily Sales Over Time', showing sales on the y-axis and date on the x-axis.
