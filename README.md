# YouTube-Playlist-downloader
Easily download all the videos of a YouTube Playlist using Python's BeautifulSoup library.

# Why this project?
I had a playlist on YouTube and wanted to download all the videos in it. I already knew Python and had heard about its BeautifulSoup Web Scraping library. Hence, I created this project and downloaded the whole playlist in one click.

# Prerequisites
1. Python 3 or above
2. BeautifulSoup4 library
3. Requests library
4. PyTube library

# Installing
1. Download and install Python 3:
  https://www.python.org/downloads/
2. BeautifulSoup is pip installable:
  in CMD: pip install beautifulsoup4
3. I’m also going to use the http requests library:
  in CMD: pip install requests
4. The other library I’ll be using allows us to extract/download video material from YouTube. It’s called PyTube and you can also get it from pip:
  in CMD: pip install pytube
  
# How to use?
1. After completing the above steps,clone the source code of this project. 
2. Open the file Downloader.py
3. In 6th line, add your Playlist url in double quotation marks ("").
  for example: url="https://www.youtube.com/playlist?list=PLWLA7WussII52VdYRn9cDHSUn*"
4. In 28th line, in myvid.download('/Github'), add your directory name in place of Github(Directory should be already present) or leave it empty to download in same directory.
5. Save the file and run in either an IDE or using cmd (whichever way you are comfortable with).

That's it! your videos will be downloaded and may take time depending on various factors like:
  i) Number of videos in the playlist
  ii) Resolution of videos
  iii) Internet speed
 
# References
https://github.com/nficano/pytube
