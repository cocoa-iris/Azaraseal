


#BerryBot 1.0


import requests
import webbrowser
import json
import time
import random

webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=【BerryBot】")

for i in range(0,50000):
  time.sleep(300)
  a=0
  a2=''
  a3='ー'
  a4=''
  a5='ω'
  a6=''
  a7=''
  a8=''
  a9='ｺﾞﾌｯ'
  while a<=15:
    k=random.randrange(0,5)
    p=random.randrange(0,2)
    if k==0:
      a2+=' '
    if k==1:
      a4+=' '
    if k==2:
      a6+=' '
    if k==3:
      a7+=' '
    if k==4:
      a8+=' '
    if p==0:
      a9='ｺﾞﾌｯ'
    else:
      a9='ｺﾞﾌｰ'
    seal='('+a2+a3+a4+a5+a6+a3+a7+'っ'+a8+')3'+a9
    if a==5:
      a3='・'
    if a==10:
      webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=(ーωーっ)3ｺﾞﾌｯ")
      break
    print(seal)
    webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message="+seal)
    a+=1











import random

for i in range(0,5):
  l=[0,1,2,3,4]
  a=0
  a2=''
  a3='ー'
  a4=''
  a5='ω'
  a6=''
  a7=''
  a8=''
  a9='ｺﾞﾌｯ'
  random.shuffle(l)
  while a<=5:
    p=random.randrange(0,2)
    print(l[a])
    k=l[a]
    if k==0:
      a2+=' '
    if k==1:
      a4+=' '
    if k==2:
      a6+=' '
    if k==3:
      a7+=' '
    if k==4:
      a8+=' '
    if p==0:
      a9='ｺﾞﾌｯ'
    else:
      a9='ｺﾞﾌｰ'
    seal='('+a2+a3+a4+a5+a6+a3+a7+'っ'+a8+')3'+a9
    if a==2:
      a3='・'
    if a==4:
      print('r')
      break
    print(seal)
    a+=1
