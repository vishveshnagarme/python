import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = "enter api key"

userwanted = input("Enter the username of the GitHub user you want to see the details of: ")
web_link = f"https://api.github.com/users/{userwanted}"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

print(f"\nFetching data for {userwanted}...")
response = requests.get(web_link, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    print("\n=== Profile Analytics ===")
    print(f"Name: {data.get('name', 'N/A')}")
    print(f"Bio: {data.get('bio', 'No bio provided.')}")
    print(f"Public Repositories: {data.get('public_repos')}")
    print(f"Followers: {data.get('followers')} | Following: {data.get('following')}")
    print(f"Profile URL: {data.get('html_url')}")
    print("Visit github.com/vishveshnagarme/python , vishvesh.nagar.me for more such stuff.")
    print("=========================")

elif response.status_code == 404:
    print(f"\nError: The user '{userwanted}' could not be found. Check the spelling!")
else:
    print(f"\nError: Unable to fetch data. Status code: {response.status_code}")