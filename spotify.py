import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

def setup_spotify():
    """
    Set up authentication with Spotify API
    """
    scope = "user-library-modify user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="write ur client",
        client_secret="write ur client secret id",
        redirect_uri="http://localhost:8888/callback"
    ))
    return sp

def remove_liked_songs(sp, num_songs):
    """
    Remove specified number of songs from Liked Songs, starting from most recently added
    """
    songs_removed = 0
    
    while songs_removed < num_songs:
        # Get current saved tracks (20 at a time is the API limit)
        results = sp.current_user_saved_tracks(limit=20, offset=0)
        tracks = results['items']
        
        if not tracks:
            print("No more tracks to remove")
            break
            
        # Get track IDs
        track_ids = [track['track']['id'] for track in tracks]
        
        try:
            # Remove tracks in batches
            sp.current_user_saved_tracks_delete(tracks=track_ids)
            songs_removed += len(track_ids)
            print(f"Removed {len(track_ids)} songs. Total removed: {songs_removed}")
            
            # Sleep to avoid hitting rate limits
            time.sleep(1)
            
        except Exception as e:
            print(f"Error removing tracks: {e}")
            time.sleep(5)  # Wait longer if there's an error
            
    return songs_removed

def main():
    # Get number of songs to remove from user
    try:
        num_songs = int(input("How many songs would you like to remove from your Liked Songs? "))
    except ValueError:
        print("Please enter a valid number")
        return
    
    # Initialize Spotify client
    try:
        sp = setup_spotify()
    except Exception as e:
        print(f"Error setting up Spotify client: {e}")
        return
    
    # Remove songs
    total_removed = remove_liked_songs(sp, num_songs)
    print(f"\nProcess complete. Removed {total_removed} songs from your Liked Songs.")

if __name__ == "__main__":
    main()
