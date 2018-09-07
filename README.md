# spotify_most-played-songs_playlist_generator
This repository contains the Python code to automatically create or update your top-tracks playlists. Information on your top-tracks statistics is fetched from your Last.fm account. This data is used to generate your top-tracks playlists.

By default this code creates/updates the following three playlists:
  * Top 10 | WEEK
  * Top 30 | MONTH
  * Top 50 | YEAR

## Usage:

First make sure you have the necessary Python libraries. The code uses among other the [Spotipy library](https://spotipy.readthedocs.io/en/latest/#). To install this on machines which already have Python and pip installed you can simply execute:

`pip install spotipy`

After this you can clone the main.py file from this repository and execute it as follows:

`python main.py <Spotify_username> <Lastfm_username>`

The first time you run the script a link will be opened in your default browser to give the application access to modify your Spotify playlists with the scope "playlist-modify-public". After giving the application access, you are directed to a link starting with http://example.com/... Copy the whole link and paste it in the terminal or command prompt to give the script the necessary permissions. This will result in your top-tracks playlists to be generated/updated.

## Further Development

It is possible to fetch the top tracks of a Spotify user directly from the Spotify account. This would using a Last.fm account in this application unnecessary. There are however only three time ranges allowed for queries in the Spotify API:

  * short_term: approximately 4 weeks
  * medium_term: approximately 6 months
  * long_term: several years

This results in less flexible and less interesting statistics compared to the time ranges allowed by the Last.fm API. It was therefore chosen to initially implement this program to use with a Last.fm account. If this is requested I could change the script to also work without a Last.fm account by only using the statistics provided by the Spotify API. 
