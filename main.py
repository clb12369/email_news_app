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
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      f"from={date}&sortBy=publishedAt&" \
      f"apiKey={api_key}&language=en"
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Make the request
response = requests.get(url, headers=headers)

# Get content in JSON (dictionary) format
content = response.json()


# Access the article titles
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = ("Subject: Today's news" + "\n"
                + body + article["title"] + "\n"
                + article["description"]+ "\n"
                + article["url"] + "\n" * 2)

print(body)
# body = body.encode("utf-8")
# send_email(message=body)
