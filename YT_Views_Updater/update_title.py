from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import json

# Define the scope (grants permission to update video titles)
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Load the credentials from the token file
with open("token.json", "r") as token_file:
    creds_data = json.load(token_file)
creds = Credentials.from_authorized_user_info(creds_data, SCOPES)

# Build the authenticated YouTube API client
youtube = build("youtube", "v3", credentials=creds)

def get_video_views(video_id):
    try:
        request = youtube.videos().list(
            part="statistics",
            id=video_id
        )
        response = request.execute()
        views = response["items"][0]["statistics"]["viewCount"]
        print(f"Current views: {views}")
        return views
    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None

def update_video_title(video_id, new_title):
    try:
        # Get the current video details (snippet)
        video_details = youtube.videos().list(
            part="snippet",
            id=video_id
        ).execute()
        
        snippet = video_details["items"][0]["snippet"]
        snippet["title"] = new_title  # Update the title

        # Update the video with the new title
        request = youtube.videos().update(
            part="snippet",
            body={
                "id": video_id,
                "snippet": snippet  # Use the modified snippet
            }
        )
        response = request.execute()
        print(f"Updated title to: {new_title}")
        return response
    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None

# Your YouTube Video ID
VIDEO_ID = "65bHF-KkocU"

# Fetch current views
views = get_video_views(VIDEO_ID)

# If views retrieved successfully, update the title
if views:
    new_title = f"My Video has {views} Views!"
    update_video_title(VIDEO_ID, new_title)
else:
    print("Failed to retrieve video views.")
