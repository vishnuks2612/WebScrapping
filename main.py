import requests
from bs4 import BeautifulSoup
import csv

# URL of the Flipkart iPad category page
url = 'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&q=ipad'

# Send a GET request to the URL
response = requests.get(url)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the iPad product containers
ipad_containers = soup.find_all('div', {'class': '_1AtVbE'})
# Create a CSV file to store the product details
csv_filename = 'flipkart_ipad_products.csv'

# Open the CSV file in write mode
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Product Name', 'Price', 'Rating', 'Features'])

    # Loop through each iPad container and extract product details
    for ipad in ipad_containers:
        try:
            product_name = ipad.find('div', {'class': '_4rR01T'}).text
            price = ipad.find('div', {'class': '_30jeq3'}).text
            rating = ipad.find('div', {'class': '_3LWZlK'}).text
            features = ipad.find('ul', {'class': '_1xgFaf'}).text.strip()

            # Write the product details to the CSV file
            csv_writer.writerow([product_name, price, rating, features])
        except AttributeError:
            continue

print('Scraping and CSV export completed successfully.')