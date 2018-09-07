# Spotify top-tracks playlists
This repository contains the Python code to automatically create or update your top-tracks playlists. Top-tracks statistics are fetched from your [Last.fm](www.last.fm) account. These statistics are then used to update your Spotify playlists.

By default this code creates/updates the following three playlists on your Spotify account:
  * Top 10 | WEEK
  * Top 30 | MONTH
  * Top 50 | YEAR

## Usage:

First make sure you have the necessary Python libraries. The code uses among other the [Spotipy library](https://spotipy.readthedocs.io/en/latest/#). To install this on machines which already have Python and pip installed you can simply execute:

```pip install spotipy```

After this you can clone the main.py file from this repository and execute it as follows:

```python main.py <Spotify_username> <Lastfm_username>```

The first time you run the script a link will be opened in your default browser to give the application access to modify your Spotify playlists with the scope "playlist-modify-public". After giving the application access, you are directed to a link starting with http://example.com/... Copy the whole link and paste it in the terminal or command prompt to give the script the necessary permissions. This will result in your top-tracks playlists to be generated/updated.

## Automation (Linux)

It is recommended to make this script run at least once a week as your top-tracks change over time. On most Linux distributions it is common to do this using [Cron](https://en.wikipedia.org/wiki/Cron). An automated job is added to the crontab (the Cron table). It is important to note that Cron jobs are executed as Root and do not necessarily use the same Python version as the user-account. It is also important to note that your Spotify access token (which you obtained when you first ran the script) is stored in the same directory from where you ran the script. Therefor it is recommended to make a simple Bash script to ensure that the cronjob executes the Python script from the directory containing the access token. 

For example on a Raspberry Pi on which main.py is stored in /home/pi/spotify_playlists/

Make a simple bash script:

```bash
$ sudo nano /home/pi/spotify_playlists/automate.sh
```

Add the following lines:

``` 
cd /home/pi/spotify_playlists

/usr/bin/python main.py <spotify_username> <lastfm_username>
```

Open the Crontab in the terminal:

```$ crontab -e```

Add the Cron job at the end of the file:

```0 8 * * * bash /home/pi/spotify_playlists/automate.sh```

This code will run every day at 8 AM (if your device is online at that time). More information on the Crontab file is found in the [Crontab documentation](https://linux.die.net/man/5/crontab). 

## Further Development

It is possible to fetch the top tracks of a Spotify user directly from the Spotify account. This would make using a Last.fm account in this application unnecessary. There are however only three time ranges allowed for queries in the Spotify API:

  * short_term: approximately 4 weeks
  * medium_term: approximately 6 months
  * long_term: several years

This results in less flexible and less interesting statistics compared to the time ranges allowed by the Last.fm API. It was therefore chosen to initially implement this program to use with a Last.fm account. If this is requested I could change the script to also work without a Last.fm account by only using the statistics provided by the Spotify API. 
