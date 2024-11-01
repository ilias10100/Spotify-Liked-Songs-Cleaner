# Spotify-Liked-Songs-Cleaner
After my Spotify account was hacked and thousands of unwanted songs were added, I created this tool to save time by automating the deletion process. This program connects to your Spotify account via the Spotify API and removes songs from the "Liked Songs" playlist in batches, allowing you to specify how many songs to delete.

# Features

Automated Song Removal: Remove any number of songs from your "Liked Songs" playlist, starting from the most recently added.
Batch Processing: Deletes songs in batches to prevent API rate limit issues.
Error Handling: Pauses and retries when errors occur to ensure reliable operation.

#Requirements

Spotipy: A lightweight Python library for the Spotify Web API.
Spotify Developer Account: You will need to register a Spotify application to obtain client_id and client_secret for authentication.

#Setup

Clone the Repository:

git clone https://github.com/yourusername/spotify-liked-songs-cleaner.git
cd spotify-liked-songs-cleaner

Install Dependencies:

pip install spotipy

Create a Spotify App:

*Go to Spotify Developer Dashboard.
*Create a new app and note down the client_id and client_secret.
*Set the Redirect URI to http://localhost:8888/callback.

Set Up Environment Variables: Create a .env file or add the following environment variables with your credentials:

*SPOTIPY_CLIENT_ID='your_client_id'
*SPOTIPY_CLIENT_SECRET='your_client_secret'
*SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

#Usage

Run the script to start removing songs from your "Liked Songs" playlist.
python main.py
You will be prompted to enter the number of songs you want to remove.

#Code Explanation

setup_spotify(): Sets up the Spotify client with the necessary permissions (user-library-read and user-library-modify) to access and modify saved tracks.
remove_liked_songs(sp, num_songs): Retrieves and deletes songs from your "Liked Songs" in batches. It uses current_user_saved_tracks to get the songs and current_user_saved_tracks_delete to remove them.
main(): Handles user input, initializes the Spotify client, and calls the song removal function.

#License

This project is licensed under the MIT License. See LICENSE for more details.

#Disclaimer
Use this tool responsibly. Removing songs is irreversible, so double-check your input to avoid deleting more songs than intended.


