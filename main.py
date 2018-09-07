#!/usr/bin/env python
import urllib, sys, os, errno
import xml.etree.ElementTree as ET
import spotipy
import spotipy.util as util
import time

#Change this if you want other top-track playlists
top_playlist_info = {"Top 10 | WEEK": ['7day',10], "Top 30 | MONTH" : ['1month', 30], "Top 50 | YEAR" : ['12month', 50]}

# Constants
LASTFM_API_KEY = 'b25b959554ed76058ac220b7b2e0a026'
SPOTIFY_SCOPE = 'playlist-modify-public'
SPOTIPY_CLIENT_API1='241fd6ca81b9433697cebae67f729bb1'
SPOTIPY_CLIENT_API2='849421fda50e4bc8b99278ee1342ece5'
SPOTIPY_REDIRECT_URI='http://example.com/callback/'

def main():

    sys_args = sys.argv
    assert len(sys_args)==3, "A Spotify and Last.fm username should be given as input \n Usage: python main.py <Spotify_username> <Lastfm_username>"
    spotify_username = sys_args[1]
    lastfm_username = sys_args[2]

    token = util.prompt_for_user_token( spotify_username ,SPOTIFY_SCOPE,client_id=SPOTIPY_CLIENT_API1,client_secret=SPOTIPY_CLIENT_API2,redirect_uri=SPOTIPY_REDIRECT_URI)
    sp = spotipy.Spotify(auth=token)
    playlists = sp.current_user_playlists()

    for playlist_key in top_playlist_info.keys():
        track_ids = []
        url = 'http://ws.audioscrobbler.com/2.0/?%s' % urllib.urlencode(dict(
            method  = 'user.gettoptracks',
            user    = lastfm_username,
            period  = top_playlist_info[playlist_key][0],
            limit   = top_playlist_info[playlist_key][1],
            api_key = LASTFM_API_KEY,
        ))

        tracks = urllib.urlopen(url)
        tree = ET.parse(tracks)
        root = tree.getroot()
        for child in root.iter('track'):
            song = child.find('name').text
            try:
                song = clean_song_name(song)
                artist = child.find('artist').find('name').text
                query = artist + " "+ song
                song_dict = sp.search( q = query, type= 'track', limit = 1)
                track_ids.append(song_dict['tracks']['items'][0]['id'])

            except:
                print("Query \"{}\" could not be answered correctly on Spotify".format(query))

        changed = False
        for playlist in playlists['items']:
            if playlist['name'] == playlist_key:
                sp.user_playlist_replace_tracks(sp.me()['id'], playlist['id'], track_ids)
                changed = True

        if not changed:
            print(playlist_key, "Playlist creation method was executed")
            playlist = sp.user_playlist_create(sp.me()['id'], playlist_key,public=True, description= "Automatically created top-tracks playlist from github.com/NelisG/spotify_top-tracks_playlists")
            sp.user_playlist_replace_tracks(sp.me()['id'], playlist['id'], track_ids)

def clean_song_name(song):
    bad_strings = [' - Remastered', ' - Original', ' - Single Version', ' - Orchestra Version', ' - Long Version' ]
    for bad_string in bad_strings:
        song = song.replace(bad_string, '')
    return song

if __name__=='__main__':
    tic = time.time()
    main()
    toc = time.time()-tic
    print("Program was run in %.2fs" %toc)
