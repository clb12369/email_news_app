import requests
import os
from dotenv import load_dotenv
from send_email import send_email

# Load environment variables
load_dotenv()

# Access the secret API key
api_key = os.environ.get("API_KEY")

# Set up date, URL, and headers
topic = "tesla"
date = "2026-09-01"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      f"from={date}&sortBy=publishedAt&" \
      f"apiKey={api_key}"
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Make the request
request = requests.get(url, headers=headers)

# Get content in JSON (dictionary) format
content = request.json()


# Access the article titles
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" * 2

body = body.encode("utf-8")
send_email(message=body)
