import requests
from functions import get_api_key, get_json_data_from_api, convert_json_to_df, convert_df_to_csv
import pandas as pd

api_calls = [0]

# Get the HOTELS in newyork near 124 Hudson Street in a radiues of 150 meters
url = "https://api.foursquare.com/v3/places/search?query=hotel&ll=40.720276093678535%2C-74.00855578601094&radius=150"
data = get_json_data_from_api(url, api_calls)

df = convert_json_to_df(data)

#for each fsq_id value in the fsq_id column, make an API call to get the tips for that place
# and then add the tips to the dataframe
for fsq_id in df['fsq_id']:
    url = f"https://api.foursquare.com/v3/places/{fsq_id}/tips"
    tips = get_json_data_from_api(url, api_calls)
    
    tips_text = [tip['text'] for tip in tips]  # Get the 'text' from each tip

    # Assign the list of tip texts to the dataframe
    df.loc[df['fsq_id'] == fsq_id, 'tips'] = ', '.join(tips_text)


print(df.head())

convert_df_to_csv(df, 'output.csv')
print("CSV file has been saved as 'output.csv'")
print("API calls made:", api_calls[0])
