import tweepy
import random
import time
import requests
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    
    # If author is "Unknown", generate a new random quote until a valid author is obtained
    while author == "Unknown":
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
    return quote, author


client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Function to tweet a random quote
def tweet_quote():
    # Get a random quote
    quote, author = get_quote()
    # Create the tweet
    tweet = f"{quote} - {author}"
    # Tweet the quote
    response = client.create_tweet(text=tweet)

# Main loop to tweet everyday
while True:
    # Get the current time
    current_time = time.strftime("%H:%M:%S", time.localtime())

    # Check if it's time to tweet (e.g., 9:00 AM)
    if current_time == "09:00:00":
        # Tweet the quote
        tweet_quote()

    # Wait for 1 second before checking the time again
    time.sleep(1)
