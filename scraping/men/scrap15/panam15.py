import pandas as pd
import requests
from bs4 import BeautifulSoup

# Specify the URL of the page containing the tables
url = 'https://en.wikipedia.org/wiki/Gymnastics_at_the_2015_Pan_American_Games_%E2%80%93_Men%27s_parallel_bars'

# Send a GET request to the URL and parse the content with BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables on the page
tables = soup.find_all('table')

# Loop through each table and save them to separate CSV files
for i, table in enumerate(tables):
    df = pd.read_html(str(table))[0]

    # Drop rows with all NaN values
    df.dropna(how='all', inplace=True)

    # Reset the index
    df.reset_index(drop=True, inplace=True)

    # Save the DataFrame to a CSV file
    csv_filename = f'table_{i}.csv'
    df.to_csv(csv_filename, index=False)

    print(f'Table {i} saved as {csv_filename}')
