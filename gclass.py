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


sheet=client.open('trial').sheet1
txt=''
count=0
e=''
i=0
f=1
pts=0
root = Tk()
def clear():
  list=root.grid_slaves()
  for l in list:
    l.destroy()

def menu():
  global e
  global i
  global f
  count=0
  e=''
  #i=0
  f=1
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

def reg():
    global i
    global txt
    global f
    i=0 
    f=1
    f1=open("user.txt",'w')
    #if txt!=' '&txt!='':
    f1.write(txt)
    f1.write(" ")
    clear()
    #else :
     #Label(root,text='invalid').grid(row=7)      


def trial():
   global e
   global i
   global count
   global f
   global pts   
   if i<=5: 
    j=random.randint(1,6)
    if j==1:
        q="Which of the following is a Palindrome number?"
        a="A.42042"
        b="B.101010"
        c="C.23232"
        d="D.01234"
        e='c'
        built(q,a,b,c,d)
    elif j==3:
        q='The country with the highest environmental performance index is...'
        a='A.France'
        b='B.Denmark'
        c='C.Switzerland'
        d='D.Finland'
        e='c'
        built(q,a,b,c,d)
    elif j==3:
        q='Which animal laughs like human being?'
        a='A.Polar Bear'
        b='B.Hyena'
        c='C.Donkey'
        d='D.Chimpanzee'
        e='b'
        built(q,a,b,c,d)
    elif j==4:
        q='Who was awarded the youngest player award in Fifa World Cup 2006?'
        a='A.Wayne Rooney'
        b='B.Lucas Podolski'
        c='C.Lionel Messi'
        d='D.Christiano Ronaldo'
        e='b'
        built(q,a,b,c,d)
    elif j==5:
        q='Which is the third highest mountain in the world?'
        a='A.Mt. K2'
        b='B.Mt. Kanchanjungha'
        c='C.Mt. Makalu'
        d='D.Mt. Kilimanjaro'
        e='b'
        built(q,a,b,c,d)
    elif j==6:
        q='What is the group of frogs known as?'
        a='A.A traffic'
        b='B.A toddler'
        c='C.A police'
        d='D.An Army'
        e='d'
        built(q,a,b,c,d)
    i=i+1

   elif f==1:
    f=2
    pts=0
    if count<2:
       clear()
       Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Sorry you are not Eligible for next round').grid(row=0)
       Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="Back",command=lambda:menu()).grid(row=2,column=0)      
    else:
       clear()
       Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Congrats you are Eligible for next round').grid(row=0)
       Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="Back",command=lambda:menu()).grid(row=2,column=0)        
       Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="PLAY",command=lambda:trial()).grid(row=2,column=2)        
   else:
    if i<=16:
     j=random.randint(1,23)
     #j=1
     if j==1:
        q="What is the National Game of England?"
        a="A.Football"
        b="B.Basketball"
        c="C.Cricket"
        d="D.Baseball"
        e='c'
        built(q,a,b,c,d)
     if j==2:
        q="Study of Earthquake is called............,"
        a="A.Seismology"
        b="B.Cosmology"
        c="C.Orology"
        d="D.Etimology"
        e='a'
        built(q,a,b,c,d)
     if j==3:
        q="Among the top 10 highest peaks in the world, how many lie in Nepal? "
        a="A.6"
        b="B.7"
        c="C.8"
        d="D.9"
        e='c'
        built(q,a,b,c,d)
     if j==4:
        q="The Laws of Electromagnetic Induction were given by?"
        a="A.Faraday"
        b="B.Tesla"
        c="C.Maxwell"
        d="D.Coulomb"
        e='a'
        built(q,a,b,c,d)
     if j==5:
        q="In what unit is electric power measured?"
        a="A.Coulomb"
        b="B.Watt"
        c="C.Power"
        d="D.Units"
        e='b'
        built(q,a,b,c,d)
     if j==6:
        q="Which element is found in Vitamin B12?"
        a="A.Zinc"
        b="B.Cobalt"
        c="C.Calcium"
        d="D.Iron"
        e='b'
        built(q,a,b,c,d)
     if j==7:
        q="What is the National Name of Japan?"
        a="A.Polska"
        b="B.Hellas"
        c="C.Drukyul"
        d="D.Nippon"
        e='d'
        built(q,a,b,c,d)
     if j==8:
        q="How many times a piece of paper can be folded at the most?"
        a="A.6"
        b="B.7"
        c="C.8"
        d="D.Depends on the size of paper"
        e='b'
        built(q,a,b,c,d)
     if j==9:
        q="What is the capital of Denmark?"
        a="A.Copenhagen"
        b="B.Helsinki"
        c="C.Ajax"
        d="D.Galatasaray"
        e='a'
        built(q,a,b,c,d)
     if j==10:
        q="Which is the longest River in the world?"
        a="A.Nile"
        b="B.Koshi"
        c="C.Ganga"
        d="D.Amazon"
        e='a'
        built(q,a,b,c,d)
     if j==11:
        q="What is the color of the Black Box in aeroplanes?"
        a="A.White"
        b="B.Black"
        c="C.Orange"
        d="D.Red"
        e='c'
        built(q,a,b,c,d)
     if j==12:
        q="Which city is known at 'The City of Seven Hills'?"
        a="A.Rome"
        b="B.Vactican City"
        c="C.Madrid"
        d="D.Berlin"
        e='a'
        built(q,a,b,c,d)
     if j==13:
        q="Name the country where there no mosquitoes are found?"
        a="A.Japan"
        b="B.Italy"
        c="C.Argentina"
        d="D.France"
        e='d'
        built(q,a,b,c,d)
     if j==14:
        q="Who is the author of 'Pulpasa Cafe'?"
        a="A.Narayan Wagle"
        b="B.Lal Gopal Subedi"
        c="C.B.P. Koirala"
        d="D.Khagendra Sangraula"
        e='a'
        built(q,a,b,c,d)
     if j==15:
        q="Which Blood Group is known as the Universal Recipient?"
        a="A.A"
        b="B.AB"
        c="C.B"
        d="D.O"
        e='b'
        built(q,a,b,c,d)
     if j==16:
        q="What is the unit of measurement of distance between Stars?"
        a="A.Light Year"
        b="B.Coulomb"
        c="C.Nautical Mile"
        d="D.Kilometer"
        e='a'
        built(q,a,b,c,d)
     if j==17:
        q="he country famous for Samba Dance is........"
        a="A.Brazil"
        b="B.Venezuela"
        c="C.Nigeria"
        d="D.Bolivia"
        e='a'
        built(q,a,b,c,d)
     if j==18:
        q="Wind speed is measure by__________?"
        a="A.Lysimeter"
        b="B.Air vane"
        c="C.Hydrometer"
        d="D.Anemometer"
        e='d'
        built(q,a,b,c,d)
     if j==19:
        q="Which city in the world is popularly known as The City of Temple?"
        a="A.Delhi"
        b="B.Bhaktapur"
        c="C.Kathmandu"
        d="D.Agra"
        e='c'
        built(q,a,b,c,d)
     if j==20:
        q="Which hardware was used in the First Generation Computer?"
        a="A.Transistor"
        b="B.Valves"
        c="C.I.C"
        d="D.S.S.I"
        e='b'
        built(q,a,b,c,d)
     if j==21:
        q="Ozone plate is being destroyed regularly because of____ ?"
        a="A.L.P.G"
        b="B.Nitrogen"
        c="C.Methane"
        d="D. C.F.C"
        e='d'
        built(q,a,b,c,d)
     if j==22:
        q="Who won the Women's Australian Open Tennis in 2007?"
        a="A.Martina Hingis"
        b="B.Maria Sarapova"
        c="C.Kim Clijster"
        d="D.Serena Williams"
        e='d'
        built(q,a,b,c,d)
     if j==23:
        q="Which film was awarded the Best Motion Picture at Oscar in 2010?"
        a="A.The Secret in their Eyes"
        b="B.Shutter Island"
        c="C.The King's Speech"
        d="D.The Reader"
        e='c'
        built(q,a,b,c,d)
     #print('hi',i,j)
    else :
     end()     
       
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
 global count
 global e
 if e==k:
   count=count+1
   right()
 else :
   wrong(e)
 return 0

def right():
  clear()
  global i
  global pts
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='CONGRATS,..!').grid(row=1,column=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Your Answer is Correct,..!').grid(row=2,columnspan=1) 
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='QUIT',command=root.destroy).grid(row=4,column=0)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='NEXT',command=lambda:trial()).grid(row=4,column=2)
  i=i+1
  pts=pts+1
  return 0

def wrong(e):  
  clear()
  global i
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='SORRY,..!').grid(row=1,column=1)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Your Answer is Wrong,..!').grid(row=2,columnspan=1) 
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='QUIT',command=root.destroy).grid(row=4,column=0)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='NEXT',command=lambda:trial()).grid(row=4,column=2)
  i=i+1
  return 0



def play():
    clear()
    reg()
    trial()


def start():
  global txt
  clear()
#  root.bind('<Return>',play())
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='G QUIZ GAME HELP').grid(row=0)
  Label(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='Register your Name').grid(row=1)
  Label(root,padx=12,bd=5,fg="black",font=('arial',20,'bold'),text='Name').grid(row=2,column=0)
  Entry(root,font=('arial',20,'bold'), textvariable=txt, bd=30,insertwidth=4,bg="sky blue").grid(row=3,columnspan=3)
  Label(root,text='').grid(row=4)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='GO BACK',command=lambda:menu()).grid(row=5,column=0)
  Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='SIGN IN',command=lambda:play()).grid(row=5,column=2)
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

#Label(root,text='hello').grid(row=0)
#Label(root,text='hello').grid(row=0)
#Label(root,text='hello').grid(row=0)
#Label(root,text='hello').grid(row=0)
#Button(root,text='clear',command=clear).grid(row=1)
menu()
root.mainloop()
