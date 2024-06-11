from google_drive_downloader import GoogleDriveDownloader as gdd
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import socket
import sys
import os.path
import pprint
from tkinter  import*
import random
import time
root = Tk()
client_secret='client-secret.json'
pp=pprint.PrettyPrinter()

scope=''
creds=''
client=''
sheet=''
sh1=''
sh2=''

def conn():
  global scope
  global creds
  global client
  global sheet
  global sh1
  global sh2
  scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  creds =ServiceAccountCredentials.from_json_keyfile_name('client-secret.json',scope)
  client=gspread.authorize(creds)
  sheet=client.open('trial')
  sh1=sheet.get_worksheet(1)
  sh2=sheet.get_worksheet(0)



pk=2
q=[]
a=[]
b=[]
c=[]
d=[]
ct=[]
#k=[]


def int_on(a):
  try:
    socket.create_connection(("www.google.com",80))
    conn()
    if a==1:
      start()
    else:
      post()
  except OSError:
    offine()

def offine():
  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Net work error ,...').grid(row=1)   
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Currently you are offline,...!').grid(row=2)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Please conntect to internet and try again').grid(row=3)      
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='BACK',command=lambda:menu()).grid(row=4)
 


def clear():
  list=root.grid_slaves()
  for l in list:
    l.destroy()

def menu():

  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G Class').grid(row=0)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='WELCOME TO THE GAME').grid(row=1)
  Label(root,text='').grid(row=2)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='START',command=lambda:int_on(1)).grid(row=3)
  Label(root,text='').grid(row=4)
  #Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='SCORE').grid(row=5)
  #Label(root,text='').grid(row=6)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' POST ',command=lambda:int_on(2)).grid(row=5)
  Label(root,text='').grid(row=6)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' HELP ',command=lambda:help()).grid(row=7)
  Label(root,text='').grid(row=8)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' QUIT ',command=root.destroy).grid(row=9)
  Label(root,text='').grid(row=10)


def post():
  clear()
  down=sh2.acell('i3').value
  m=[]
  jum=0
 
  f=sh2.range(down)
  for ra in f:
      	 m.append(ra.value)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G Class').grid(row=0)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Available materials').grid(row=1)
  Label(root,text='').grid(row=2)
  le=len(m)
  while jum<le:
        Label(root,padx=12,bd=5,fg="black",font=('arial',20,'bold'),text=m[jum]).grid(row=jum+2,column=1)
        Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Download',command=lambda:menu()).grid(row=jum+2,column=2)
        jum=jum+2
  Label(root,text='').grid(row=jum+2)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='GO BACK',command=lambda:menu()).grid(row=jum+3)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' QUIT ',command=root.destroy).grid(row=jum+3,column=2)
  Label(root,text='').grid(row=jum+4)  

#def bnd(x,y):
   




def start():
  k=StringVar()
  f=StringVar()
  clear()
  #root.bind('<Return>',play())
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G Class Log in').grid(row=0)
  Label(root,padx=12,bd=5,fg="black",font=('arial',20,'bold'),text='Roll No').grid(row=1,column=0)
  Entry(root,font=('arial',20,'bold'), textvariable=k, bd=30,insertwidth=4,bg="sky blue").grid(row=3,columnspan=3)
  Label(root,text='').grid(row=4)
  Label(root,padx=12,bd=5,fg="black",font=('arial',20,'bold'),text='Password').grid(row=5,column=0)
  Entry(root,show='*',font=('arial',20,'bold'), textvariable=f, bd=30,insertwidth=4,bg="sky blue").grid(row=6,columnspan=3)
  Label(root,text='').grid(row=7)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='GO BACK',command=lambda:menu()).grid(row=8,column=0)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='SIGN IN',command=lambda:log(k.get(),f.get())).grid(row=8,column=2)
  Label(root,text='').grid(row=8,column=3)
  Label(root,text='').grid(row=9)


def log(a,b):
      global pk
      clear()
      rol=[]
      pas=[]
      a=a.upper()
      b=b.upper()
      if len(a)==6 and len(b)==6 :
       f=sh1.range('A3:A52')
       for ra in f:
       	 rol.append(ra.value)
       y=sh1.range('B3:B52')
       for ra1 in y:
      	 pas.append(ra1.value)
       for m,n in zip(rol,pas):
          pk=pk+1
          if m==a and n==b:
             ready(0)
             break
       else :
             wrong()
      else :
             wrong()
  
def ready(i):
  global q
  global a
  global b
  global c
  global d
  f=sh2.range('b4:b13')
  for ra in f:
      	 q.append(ra.value)
  f=sh2.range('c4:c13')
  for ra in f:
      	 a.append(ra.value)
  f=sh2.range('d4:d13')
  for ra in f:
      	 b.append(ra.value)
  f=sh2.range('e4:e13')
  for ra in f:
      	 c.append(ra.value)
  f=sh2.range('f4:f13')
  for ra in f:
      	 d.append(ra.value)
  if(i<10):
   built(q[i],a[i],b[i],c[i],d[i],i)
  else:
    fin()

def fin():
    global ct
    i=0
    st='c'+str(pk)+':L'+str(pk)
    cl=sh1.range(st)
    for x in cl:
      x.value=ct[i]
      i=i+1
    sh1.update_cells(cl)
    clear()
    Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G Class').grid(row=1)   
    Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='You suceesflly finish your quiz ,...!').grid(row=2)
    Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Click submit to see your score').grid(row=3)      
    Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='SUBMIT',command=lambda:score()).grid(row=4)

def score():
  sk='m'+str(pk)
  score=sh1.acell(sk).value  
  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Your Score is ,...!').grid(row=2)   
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=score).grid(row=3)
  
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='BACK',command=lambda:menu()).grid(row=4)


def wrong():
  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='You have entered a wrong user id').grid(row=1)   
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='or a wrong password').grid(row=2)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Please enter a correct id and password').grid(row=3)      
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='BACK',command=lambda:menu()).grid(row=4)


def built(q,a,b,c,d,i):
  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G Class').grid(row=0,columnspan=4)    
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=q).grid(row=2,columnspan=4)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=3)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=a,command=lambda:val('a',i)).grid(row=4,column=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=4,column=2)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=b,command=lambda:val('b',i)).grid(row=4,column=3)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=4,column=4)

  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=5)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=c,command=lambda:val('c',i)).grid(row=6,column=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=6,column=2)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=d,command=lambda:val('d',i)).grid(row=6,column=3)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=6,column=4)

  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=7)
  return 0

def val(k,i):
 global ct
 ct.append(k)
 ready(i+1)



def help():
  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G CLASS HELP').grid(row=0)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='- ---- ---- ----').grid(row=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='An Online Classroom to improve your skills').grid(row=2)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='You can find the Study Materials at Post you can download and study it').grid(row=3)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' The downloaded file will be located at your local directory ').grid(row=4)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Click Start Button to have quiz The score will be displayed at last').grid(row=5)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='The questions and study materials will be updated regularly').grid(row=6)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='You must have internet connection to perform this operations').grid(row=7)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='ABOUT').grid(row=8)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='All credits goes to Artist G').grid(row=9)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Version - 1.2.5').grid(row=10)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='GO BACK',command=lambda:menu()).grid(row=11)  


root.title('G Class')
menu()
root.mainloop()





