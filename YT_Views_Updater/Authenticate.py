from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Define the scope (grants permission to update video titles)
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Authenticate user via OAuth 2.0 (First-time authentication opens a browser window)
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
creds = flow.run_local_server(port=0)

# Save the credentials to a file
with open("token.json", "w") as token_file:
    token_file.write(creds.to_json())

print("Refresh token saved to token.json")