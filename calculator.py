from Tkinter import *
import math
def btnClick(numbers) :
  global operator
  operator=operator + str (numbers)
  text_Input.set(operator)

def btnEnter():
   if operator!="" :
       btnEqualsInput() 
   else :
       text_Input.set(0)

def btnClearDisplay():
   global operator
   operator=""
   text_Input.set("")

def btnEqualsInput():
   global operator
   operator=text_Input.get()
   sumup=str(eval(operator))
   text_Input.set(sumup)
   operator=""

def btnfact() :
   global operator
   #key=operator+"!"
   operator=str(math.factorial(int(operator)))
   text_Input.set(operator)
cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()
#entryk=Entry(cal
#cal.wm_iconbitmap('alien.ico')
txtDisplay=Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd=30,insertwidth=4,bg="sky blue",justify='right').grid(columnspan=4)
cal.bind('<Return>',btnEnter())
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="light blue",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="sky blue",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="sky blue",command=lambda:btnClick(9)).grid(row=1,column=2)
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="sky blue",command=lambda:btnClick(6)).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="sky blue",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="sky blue",command=lambda:btnClick(4)).grid(row=2,column=2)
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="sky blue",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="sky blue",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="sky blue",command=lambda:btnClick(3)).grid(row=3,column=2)
btna=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="sky blue",command=lambda:btnClick('+')).grid(row=4,column=3)
btns=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=" -",bg="sky blue",command=lambda:btnClick('-')).grid(row=3,column=3)
btnm=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="x",bg="sky blue",command=lambda:btnClick('*')).grid(row=2,column=3)
btnd=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=" /",bg="sky blue",command=lambda:btnClick('/')).grid(row=1,column=3)
btn0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="sky blue",command=lambda:btnClick(0)).grid(row=4,column=1)
btne=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="sky blue",command=lambda:btnEqualsInput()).grid(row=4,column=2)
btnt=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=". ",bg="sky blue",command=lambda:btnClick('.')).grid(row=4,column=0)
btnp=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',8,'bold'),text="Pow",bg="sky blue",command=lambda:btnClick('**')).grid(row=5,column=2)
btnc=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',7,'bold'),text="Clear",bg="sky blue",command=lambda:btnClearDisplay()).grid(row=5,column=0)
btno=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',8,'bold'),text="Mod",bg="sky blue",command=lambda:btnClick('%')).grid(row=5,column=3)
btnf=Button(cal,padx=16,pady=12,bd=8,fg="black",font=('arial',8,'bold'),text="Fact",bg="sky blue",command=lambda:btnfact()).grid(row=5,column=1)



cal.mainloop()
