from bs4 import BeautifulSoup as bs		# importing BeautifulSoup library
import requests				# importing requests library
from pytube import YouTube			# importing Youtube library from pytube package

# Enter the url of the playlist to be downloaded.
url="https://www.youtube.com/playlist?list=PLWLA7WussII52VdYRn9cDHSUn0QwRpZiv"	

r = requests.get(url)				
page=r.text
soup=bs(page,'html.parser')

# Once you’ve used BeautifulSoup to parse the html, you can extract all kinds of things. 
# For this example I’m just looking at the videos' links.

vids=soup.findAll('a',class_="pl-video-title-link")	# this is the class which is present only in the playlist videos' <a> tag.

#storing all the videos in videolist array(or list).
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href'][:21]	# 21 is the length of the video link and is appended with youtube.com.
    videolist.append(tmp)

# Loop over all the web-links in our videolist and download the video for each one.
for item in videolist:
    yt = YouTube(item)			# initiate the class.
 
    myvid = yt.streams.first()			# the first stream usually contains the video with best video and audio quality.
    myvid.download('/Github')			# downloading the video and saving it to 'Github' folder. Keep download() empty if you want to download in same folder.
    
print("All videos are downloaded !")