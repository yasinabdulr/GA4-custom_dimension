from flask import Flask, request, redirect, jsonify
import requests
import json
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Replace these with your client details
client_id = '<FROM GOOGLE API CONSOLE>'
client_secret = '<FROM GOOGLE API CONSOLE>'

# OAuth endpoints given in the Google API documentation
authorization_base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
token_url = 'https://oauth2.googleapis.com/token'
scope = ["https://www.googleapis.com/auth/analytics.edit"]

# Redirect URI specified when setting up the application
redirect_uri = 'http://127.0.0.1:5000/callback'

# Initialize the OAuth client
oauth = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, scope=scope)

# List of property IDs
property_ids = [
    '<PROPERTY ID 1>',
    '<PROPERTY ID 2>'
]

# Add a single or list of custom dimensions here
custom_dimensions = [
    {
    "displayName": "<DISPLAY NAME 1>",
    "description": "<DESCRIPTION 1>",
    "parameterName": "PARAMETER 1",
    "scope": "EVENT"
    },
    {
    "displayName": "<DISPLAY NAME 2>",
    "description": "<DESCRIPTION 2>",
    "scope": "USER",
    "parameterName": "PARAMETER 2"
    }
  ]

# -------------------------------------- IMPORTANT: Change this to the list of property IDs you want to create the custom dimensions for ------------------------------------------------------
property_ids = property_ids

@app.route("/")
def hello():
    """Present the user with a link to authenticate with Google."""
    authorization_url, state = oauth.authorization_url(authorization_base_url)
    return f'<a href="{authorization_url}">Click here to authenticate with Google</a>'

@app.route("/callback")
def callback():
    """The callback route, the user is redirected here from Google with the code."""
    token = oauth.fetch_token(token_url, authorization_response=request.url, client_secret=client_secret)
    return redirect("/create_custom_dimensions")

@app.route("/create_custom_dimensions")
def create_custom_dimensions():
    """Create custom dimensions for each property ID."""
    results = []
    for property_id in property_ids:
        for dimension in custom_dimensions:
            url = f"https://analyticsadmin.googleapis.com/v1beta/properties/{property_id}/customDimensions"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {oauth.token['access_token']}"
            }
            response = requests.post(url, headers=headers, data=json.dumps(dimension))
            results.append({
                'property_id': property_id,
                'dimension': dimension['displayName'],
                'status_code': response.status_code,
                'response': response.json()
            })
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
