import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
apikey = os.getenv('api_key')

# Fetch data from API
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MSFT&apikey={apikey}'
response = requests.get(url)
data = response.json()

# Extract Weekly Time Series
weekly_time_series = data.get('Weekly Time Series', {})

# Check if data is available
if weekly_time_series:
    # Create a list of rows
    rows = []
    for date, values in weekly_time_series.items():
        rows.append({
            'week': date,
            'open': float(values['1. open']),
            'high': float(values['2. high']),
            'low': float(values['3. low']),
            'close': float(values['4. close']),
            'volume': int(values['5. volume'])
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(rows)
    
    # Convert 'week' column to datetime format
    df['week'] = pd.to_datetime(df['week'])
    
    # Display the DataFrame
    print(df.head())
    
    # Save the DataFrame to a CSV file
    df.to_csv('msftstock.csv', index=False)
    print(f"Data successfully saved to 'msftstock.csv'")
else:
    print("No data found in Weekly Time Series.")
