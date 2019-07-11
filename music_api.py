import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


os.environ["SPOTIPY_CLIENT_ID"] = '5dc240cf3116414fae30289c9b21f890'
os.environ["SPOTIPY_CLIENT_SECRET"] = '4f3d1b2529f147d1bddf87a6f6d8fd84'
os.environ["SPOTIPY_REDIRECT_URI"] = 'https://google.com/'

# Get the username from terminal
username = '21n56cpf3ejqfcqlpfzzixqfy'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'


def Spotify():
# Erase cache and prompt for user permission
    stuff = []
    try:
        token = util.prompt_for_user_token(username, scope) # add scope
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope) # add scope

    # Create our spotify object with permissions
    spotifyObject = spotipy.Spotify(auth=token)

    # Get current device
    devices = spotifyObject.devices()
    deviceID = devices['devices'][0]['id']

    # Current track information
    track = spotifyObject.current_user_playing_track()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']

    if artist != "":
        # print("Currently playing " + artist + " - " + track)
        stuff.append("Currently playing " + artist + " - " + track)

    # User information
    user = spotifyObject.current_user()
    displayName = user['display_name']
    followers = user['followers']['total']

    # Loop
    # while 1:
        # Main Menu
        # print()
        # print(">>> Welcome to Spotipy " + displayName + "!")
        # print(">>> You have " + str(followers) + " followers.")
        # print()
        # print("0 - Search for an artist")
        # print("1 - exit")
        # print()
        # choice = input("Your choice: ")

    stuff.append("Welcome to Spotipy " + displayName + "!")
    stuff.append("You have " + str(followers) + " followers.")

    #     if choice == "0":
    #         print()
    #         searchQuery = input("Ok, what's their name?: ")
    #         print()

    #         # Get search results
    #         searchResults = spotifyObject.search(searchQuery,1,0,"artist")

    #         # Artist details
    #         artist = searchResults['artists']['items'][0]
    #         print(artist['name'])
    #         print(str(artist['followers']['total']) + " followers")
    #         print(artist['genres'][0])
    #         print()
    #         webbrowser.open(artist['images'][0]['url'])
    #         artistID = artist['id']


    #         # Album and track details
    #         trackURIs = []
    #         trackArt = []
    #         z = 0

    #         # Extract album data
    #         albumResults = spotifyObject.artist_albums(artistID)
    #         albumResults = albumResults['items']

    #         for item in albumResults:
    #             print("ALBUM: " + item['name'])
    #             albumID = item['id']
    #             albumArt = item['images'][0]['url']

    #             # Extract track data
    #             trackResults = spotifyObject.album_tracks(albumID)
    #             trackResults = trackResults['items']

    #             for item in trackResults:
    #                 print(str(z) + ": " + item['name'])
    #                 trackURIs.append(item['uri'])
    #                 trackArt.append(albumArt)
    #                 z+=1
    #             print()

    #         # See album art
    #         while True:
    #             songSelection = input("Enter a song number to see album art and play the song (x to exit): ") # and play the song
    #             if songSelection == "x":
    #                 break
    #             trackSelectionList = []
    #             trackSelectionList.append(trackURIs[int(songSelection)])
    #             spotifyObject.start_playback(deviceID, None, trackSelectionList) # added
    #             webbrowser.open(trackArt[int(songSelection)])

    #     if choice == "1":
    #         break
    return stuff

        # print(json.dumps(trackResults, sort_keys=True, indent=4))


# print(Spotify())