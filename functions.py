from dotenv import load_dotenv
import os
import pandas as pd
import requests

def get_api_key():
    # Load environment variables from the .env file
    load_dotenv()

    # Get the API key from the environment variable
    api_key = os.getenv('API_KEY')  # Fetch the API key

    if api_key is None:
        print("API key is missing in the .env file!")
        exit()
    return api_key

def convert_json_to_df(data):
    if data:
        flattened_data = []
        
        # Check if 'results' key exists (Type 1 JSON structure)
        if isinstance(data, dict) and 'results' in data:
            places = data['results']
        # Otherwise, assume it's a list (Type 2 JSON structure)
        else:
            places = data

        # Iterate over each place in 'places' (works for both Type 1 and Type 2)
        for place in places:
            # Extract the required fields based on Type 1 or Type 2 structure
            if 'fsq_id' in place:  # Type 1 (place has 'fsq_id' and 'categories')
                place_data = {
                    'fsq_id': place['fsq_id'],
                    'name': place['name'],
                    'address': place['location']['address'] if 'location' in place else None,
                    'locality': place['location']['locality'] if 'location' in place else None,
                    'country': place['location']['country'] if 'location' in place else None,
                    'formatted_address': place['location']['formatted_address'] if 'location' in place else None,
                    'latitude': place['geocodes']['main']['latitude'] if 'geocodes' in place else None,
                    'longitude': place['geocodes']['main']['longitude'] if 'geocodes' in place else None,
                    'distance': place['distance'] if 'distance' in place else None,
                    'link': place['link'],
                    'categories': [category['name'] for category in place['categories']]  # Extract category names
                }
            elif 'id' in place:  # Type 2 (place has 'id' and 'text')
                place_data = {
                    'id': place['id'],
                    'created_at': place['created_at'],
                    'text': place['text']
                }
            flattened_data.append(place_data)
        
        # Convert the list of flattened data into a DataFrame
        df = pd.DataFrame(flattened_data)
        return df
    else:
        print("No data available to save.")

def convert_df_to_csv(df, filename):
    # Save the DataFrame to CSV
    df.to_csv(filename, index=False)
    # print("CSV file has been saved as 'output.csv'")

def get_json_data_from_api(url, api_calls):
    api_key = get_api_key()

    headers = {
        "Accept": "application/json",
        "Authorization": api_key
    }

    # Make the GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        # print(data)
    else:
        print(f"Error: {response.status_code}")

    api_calls[0] += 1
    return data
