import requests
import base64

# CREATE POSTS

city_data_list = []

cities = [{"cityName": "Byron Center", "state": "Michigan", "abrv":"MI", "parent":1379, "slug": "byron-center" }, ]


for city in cities:
    city_data = {
        "city_name": city['cityName'],
        "title": f"API Test, Plese Ignore {city['cityName']} ",
        "content": f"This is a test",
        "status": "draft",
        "template": "subpage-siderbar-template",
        "parent": city["parent"]
    }

    city_data_list.append(city_data)

# SEND POSTS

# WordPress site URL
url = "URL"

# User credentials for Basic Auth
username = "USERNAME"
password = "PASSWORD"

# Encode credentials
credentials = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')

# Headers for the request
headers = {
    'Authorization': f'Basic {credentials}',
    'Content-Type': 'application/json'
}

# Post data
posts_data = city_data_list
for post_data in posts_data:
    # Make the POST request

    response = requests.post(url, headers=headers, json=post_data)

    # Check the response
    if response.status_code == 201:
        print(f"{post_data['city_name']} post created successfully.")
        print("Post ID:", response.json().get('id'))
    else:
        print("Failed to create post.")
        print("Status code:", response.status_code)
        print("Response:", response.text)
