import requests
from requests.auth import HTTPBasicAuth

consumer_key = "I7qtM5EaaF50VJr4Rn3BJQ7vHAwnsdpx"
consumer_secret = "UWfpwANAfGMMHL2v"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print (r.text)