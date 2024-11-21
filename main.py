import requests

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('API_KEY')  # Fetch the API key

if api_key is None:
    print("API key is missing in the .env file!")
    exit()

# The base URL for the API endpoint (for Foursquare venue search)
url = 'https://api.foursquare.com/v3/places/search'

headers = {
    "Accept": "application/json",
    "Authorization": api_key
}

# Make the GET request to the API
response = requests.get(url, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")

