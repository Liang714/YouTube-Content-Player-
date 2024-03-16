from importlib.resources import path
import os
from unicodedata import name
os.add_dll_directory("C:\Program Files\VideoLAN\VLC")
import vlc
import requests
import time
import random
import re,subprocess,urllib.parse,urllib.request
import pafy

def play(song,n):
        query_string = urllib.parse.urlencode({"search_query": song})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        video = pafy.new(clip2) 
        song_title=video.title
        if n==1:
           videolink = video.getbest()
           print("Video Mode")
           print(f"{song_title} is playing...")
        else:
           videolink =video.getbestaudio()
           print("Audio Mode")  
           print(f"{song_title} is playing..")  
        media = vlc.MediaPlayer(videolink.url) 
        media.play()
        time.sleep(10)
        media.stop()
while True:
   print('Welcome to Muse Music Player')
   print('>>>Menu')
   print('Search Music by Song Name>>>1')
   print('Search Music by Categories>>>2')
   print('Leave>>>3') 
   pick=int(input('Pick the number:'))
   if pick==1:
      print("Enter 1 for video and 2 for only audio")
      song=input("Enter the song name:")
      n=int(input("Enter the number:"))
      play(song,n)
   if pick==2:
      m_lst=['當個一日MC','今晚跟我R&B','那些年我們一起追的劇','動漫電影主題曲','KTV大魔王','想和你一起唱','想哭就點這','電影主題曲','V廚從聽歌開始','動漫神曲','日本千萬點閱','那些迷因從哪來']
      print("1-當個一日MC")
      print("2-今晚跟我R&B")
      print("3-那些年我們一起追的劇")
      print("4-動漫電影主題曲")
      print("5-KTV大魔王")
      print("6-想和你一起唱")
      print("7-想哭就點這")
      print("8-電影主題曲")
      print("9-V廚從聽歌開始")
      print("10-動漫神曲")
      print("11-日本千萬點閱")
      print("12-那些迷因從哪來")
      mood=int(input("Pick one from the categories:"))
      f_name=m_lst[mood-1]
      print("Your pick is:",f_name)
      fo=open(f"{f_name}.txt","r+",encoding='utf-8',errors='ignore')
      print(f_name,"songlist:")
      song_list=fo.readlines()
      for i,j in enumerate(song_list):
         print("{}-{}".format(i+1,j))
      song_num=int(input("Pick a song by number:"))
      song_name=song_list[song_num-1] 
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      song1=""
      for char in song_name:
         if char not in punctuations:
            song1=song1+char
      song1=''.join(song1.split()).lower()
      n1=int(input("Enter 1 for video and 2 for only audio:"))
      play(song1,n1)
   if pick==3:
      print("Closing Muse Music Player....")
      break          
