import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import sys
import os.path
import pprint
from tkinter  import*
import random
import time
client_secret='client-secret.json'
pp=pprint.PrettyPrinter()

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds =ServiceAccountCredentials.from_json_keyfile_name('client-secret.json',scope)
client=gspread.authorize(creds)


sheet2=client.open('trial')
sheet2=client.open('trial')
sh1=sheet.get_worksheet(1)
sh2=sheet.get_worksheet(0)
q=[]
a=[]
b=[]
c=[]
d=[]
ct=[]

root = Tk()

def clear():
  list=root.grid_slaves()
  for l in list:
    l.destroy()

def menu():

  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G QUIZ GAME').grid(row=0)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='WELCOME TO THE GAME').grid(row=1)
  Label(root,text='').grid(row=2)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='START',command=lambda:start()).grid(row=3)
  Label(root,text='').grid(row=4)
  #Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='SCORE').grid(row=5)
  #Label(root,text='').grid(row=6)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' HELP ',command=lambda:help()).grid(row=5)
  Label(root,text='').grid(row=6)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' QUIT ',command=root.destroy).grid(row=7)
  Label(root,text='').grid(row=8)  


def end():
 global pts
 clear()
 Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G QUIZ GAME RESULT').grid(row=0,columnspan=3)    
 Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Your Score is').grid(row=1,column=0)
 Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=pts*100).grid(row=1,column=1)
 Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="BACK",command=lambda:menu()).grid(row=4,column=0) 
 chk()

def chk():
 global pts
 s=pts*100
 f2=open("user.txt",'r')
 



def built(q,a,b,c,d):
  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G QUIZ GAME HELP').grid(row=0,columnspan=3)    
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=q).grid(row=2)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=3)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=a,command=lambda:val('a')).grid(row=4,column=0)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=b,command=lambda:val('b')).grid(row=4,column=2)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='   ').grid(row=4,column=3)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=5)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=c,command=lambda:val('c')).grid(row=6,column=0)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=d,command=lambda:val('d')).grid(row=6,column=2)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='').grid(row=7)
  return 0

def val(k):
 global ct
 ct.append(k)
 return 0


def play(a,b):
    clear()
   
    rol=[]
   for cell in :
	 print (cell.value)
    pass=[]
    l=a[4]
    if l<=10:
      f=sh.range('A3:A12')
     for ra in f:
	 rol.append(ra.value)
     y=sh.range('B3:B12')
     for ra1 in y:
	 pass.append(ra1.value)
    for m,n in zip(rol,pass):
       if m==a and n==b:
         ready()
    else :
         wrong()
          

    else if  l<=20:
      f=sh.range('A13:A22')
     for ra in f:
	 rol.append(ra.value)
     y=sh.range('B13:B22')
     for ra1 in y:
	 pass.append(ra1.value)
    else if l<=30:
      f=sh.range('A23:A32')
     for ra in f:
	 rol.append(ra.value)
     y=sh.range('B23:B32')
     for ra1 in y:
	 pass.append(ra1.value)
    else if l<=40:
      f=sh.range('33:A42')
     for ra in f:
	 rol.append(ra.value)
     y=sh.range('B33:B42')
     for ra1 in y:
	 pass.append(ra1.value)
    else if l<=50:
      f=sh.range('A43:A52')
     for ra in f:
	 rol.append(ra.value)
     y=sh.range('B43:B52')
     for ra1 in y:
	 pass.append(ra1.value)
    else :
      wrong()

def start():
  k=''
  f=''
  clear()
  root.bind('<Return>',play())
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G Class').grid(row=0)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Log in').grid(row=1)
  Label(root,padx=12,bd=5,fg="black",font=('arial',20,'bold'),text='Roll No').grid(row=2,column=0)
  Entry(root,font=('arial',20,'bold'), textvariable=k, bd=30,insertwidth=4,bg="sky blue").grid(row=3,columnspan=3)
  Label(root,text='').grid(row=4)
   Label(root,padx=12,bd=5,fg="black",font=('arial',20,'bold'),text='Password').grid(row=5,column=0)
  Entry(root,font=('arial',20,'bold'), textvariable=f, bd=30,insertwidth=4,bg="sky blue").grid(row=6,columnspan=3)
  Label(root,text='').grid(row=7)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='GO BACK',command=lambda:menu()).grid(row=5,column=0)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='SIGN IN',command=lambda:play(k,f)).grid(row=5,column=2)
  Label(root,text='').grid(row=5,column=3)
  Label(root,text='').grid(row=6)

def help():
  clear()
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G QUIZ GAME HELP').grid(row=0)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='- ---- ---- ----').grid(row=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='There are two rounds in the game, WARMUP ROUND & CHALLANGE ROUND').grid(row=2)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='In warmup round you will be asked a total of 3 questions to test your general knowledge.').grid(row=3)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=' You will be eligible to play the game if you can give atleast 2').grid(row=4)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='right answers otherwise you can not play the Game.........').grid(row=5)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Your game starts with the CHALLANGE ROUND. In this round you will be asked total 10 questions').grid(row=6)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='each right answer will be awarded $100,000.By this way you can win upto ONE MILLION cash prize').grid(row=7)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='You will be given 4 options and you have to press A, B ,C or D for theright option').grid(row=8)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='You will be asked questions continuously if you keep giving the right answers.').grid(row=9)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='No negative marking for wrong answers').grid(row=10)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='GO BACK',command=lambda:menu()).grid(row=11)  

menu()
root.title('G Class')
root.mainloop()
