import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = "https://thegymter.net/the-best-scores-in-2023/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the specified class
    table = soup.find('table')

    # Initialize empty lists to store the data
    rank_list = []
    athlete_list = []
    nation_list = []
    meet_list = []
    score_list = []

    # Loop through the rows of the table
    for row in table.find_all('tr'):
        # Extract the data from each cell in the row
        cells = row.find_all('td')
        if len(cells) == 5:
            rank = cells[0].text.strip()
            athlete = cells[1].text.strip()
            nation = cells[2].text.strip()
            meet = cells[3].text.strip()
            score = cells[4].text.strip()

            # Append the data to the respective lists
            rank_list.append(rank)
            athlete_list.append(athlete)
            nation_list.append(nation)
            meet_list.append(meet)
            score_list.append(score)

    # Save the data to a CSV file
    with open("best_scores2023.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["Rank", "Athlete", "Nation", "Meet", "Score"])
        for i in range(len(rank_list)):
            writer.writerow([rank_list[i], athlete_list[i],
                            nation_list[i], meet_list[i], score_list[i]])

    print("Data saved to best_scores2023.csv successfully.")
else:
    print("Failed to retrieve the webpage.")
