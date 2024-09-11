a=0
a2=''
a3='ー'
a4=''
a5='ω'
a6=''
a7=''
a8=''
import random
while a<=15:
  k=random.randrange(0,5)
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
  seal='('+a2+a3+a4+a5+a6+a3+a7+'っ'+a8+')3'
  if a==5:
    a3='・'
  if a==10:
    print('(ーωーっ)3ｺﾞﾌｯ')
    break
  print(seal)
  a+=1
