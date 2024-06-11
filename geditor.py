import os
from Tkinter import *
import tkFileDialog
from tkMessageBox import *
from tkFileDialog import askopenfilename
import tkMessageBox
rt=Tk()
#rt.geometry("800x800") 
filename=''
text=Text(rt)
text.pack(expand=True,fill=BOTH)
#text.grid(columnspan=800,rowspan=800)
i=0
savelocation='**'
rt.configure(background='white')
popup=Menu(rt,tearoff=0)
popup.add_command(label='new',accelerator='Ctrl+N',command=lambda:new())
popup.add_command(label='Save',accelerator='Ctrl+S',command=lambda:save())
popup.add_command(label='delete')
popup.add_separator()
popup.add_command(label='cut',accelerator='Ctrl+X')
popup.add_command(label='copy',accelerator='Ctrl+C')
popup.add_command(label='paste',accelerator='Ctrl+V')




def key(event):
    global i
    i=i+1
#    print "pressed", repr(event.char)
 #   print i

def motion(event):
  try:
    popup.tk_popup(event.x_root,event.y_root,0)
  #  popup.mainloop()
  finally:
   popup.grab_release()

text.bind("<Key>", key)
text.bind("<Button-3>",motion)



def newe(event):
 new()

def new():
 global savelocation
 if check()==True:
  if len(text.get('1.0', END+'-1c')) > 0:
   if tkMessageBox.askyesno("Save?", "Do you wish to save?"):
    saveas()
    text.delete('1.0', END)
   else:
    text.delete('1.0', END)
     
 else:
    text.delete('1.0', END)
 savelocation='**'
 rt.title('G Editor 2k ~'+savelocation)
def check():
 global i
 if i!=0:
   return True
 else:
   return False


def fopen():
 new()
 filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("text files","*.txt"),("all files","*.*")))
 f=open(filename)
 rt.title('G Editor 2k ~'+filename)
 text.insert(INSERT, f.read())

def saveas():
 global text
 global savelocation
 temp=savelocation
 t = text.get("1.0", "end-1c")
 try:
  savelocation=tkFileDialog.asksaveasfilename()
  file1=open(savelocation, "w+")
  file1.write(t)
  file1.close()
  rt.title('G Editor 2k ~'+savelocation)
 except:
   savelocation=temp

def save():
 global savelocation
 temp=savelocation
 global text
 t = text.get("1.0", "end-1c")
 try:
  if check()==True and savelocation=='**':
   savelocation=tkFileDialog.asksaveasfilename()
  file1=open(savelocation, "w+")
  file1.write(t)
  file1.close()
  rt.title('G Editor 2k ~'+savelocation)
 except:
   savelocation=temp
  
def quit(event):
  rt.destroy()
def feopen(event):
  fopen()
def esave(event):
   save()
def esaveas(event):
   saveas()

#key binds
rt.bind('<Control-n>', newe)
rt.bind('<Control-N>', newe)
rt.bind('<Control-q>', quit)
rt.bind('<Control-Q>', quit)
rt.bind('<Control-O>', feopen)
rt.bind('<Control-o>', feopen)
rt.bind('<Control-s>', esave)
rt.bind('<Control-S>', esave)
rt.bind('<Control-Shift-s>', esaveas)
rt.bind('<Control-Shift-S>', esaveas)

fmenu=Menu(rt)
emenu=Menu(rt)
hmenu=Menu(rt)
amenu=Menu(rt)
smenu=Menu(rt)
rt.title('G Editor 2k ~'+savelocation)
rt.config(menu=fmenu)
filemenu=Menu(fmenu)
fmenu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label='New',accelerator='Ctrl+N',command=new)
filemenu.add_command(label='Open',accelerator='Ctrl+O',command=fopen)
filemenu.add_command(label='Save',accelerator='Ctrl+S',command=lambda:save())
filemenu.add_command(label='Save As',accelerator='Ctrl+Shift+S',command=lambda:saveas())
filemenu.add_separator()
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',command=rt.destroy)

editmenu=Menu(emenu)
fmenu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label='Undo')
editmenu.add_command(label='Redo')
editmenu.add_command(label='Delete')
editmenu.add_separator()
editmenu.add_command(label='Cut',accelerator='Ctrl+X',command=rt.event_generate("<<Paste>>"))
editmenu.add_command(label='Copy',accelerator='Ctrl+C')
editmenu.add_command(label='Paste',accelerator='Ctrl+V')
editmenu.add_separator()
editmenu.add_command(label='Select All')
editmenu.add_command(label='Font')
editmenu.add_command(label='Size')

searmenu=Menu(smenu)
fmenu.add_cascade(label='Search',menu=searmenu)
searmenu.add_command(label='Find')
searmenu.add_command(label='Replace')
searmenu.add_command(label='Goto')

def call():
   root=Tk()
   root.title('G Worlds')
   root.configure(background='white')
   Label(root,padx=16,bd=8,fg="blue",bg='white',font=('URW Chancery L',20,'bold'),text='You are using editor 2k with lisence of trial version,...').grid(row=1,column=1,columnspan=3)
   Label(root,padx=16,bd=8,fg="blue",bg='white',font=('URW Chancery L',20,'bold'),text='No contents and documentation is found for this version ,... ').grid(row=2,column=1,columnspan=3)
   Label(root,padx=16,bd=8,fg="blue",bg='white',font=('URW Chancery L',20,'bold'),text='Upgrade to premium to enable this options ,... !').grid(row=3,column=1,columnspan=3)
   Button(root,padx=16,bd=8,fg='blue',bg='white',font=('URW Chancery L',20,'bold'),text='Back',command=root.destroy).grid(row=5,column=2)
   root.mainloop()


helpmenu=Menu(hmenu)
fmenu.add_cascade(label="help",menu=helpmenu)
helpmenu.add_command(label='content',command=call)
helpmenu.add_command(label='lisence',command=call)
helpmenu.add_command(label='documentation',command=call)


def aus():
   root=Tk()
   root.title('About us,... (G Worlds)')
   root.configure(background='white')
   Label(root,padx=16,bd=8,fg="blue",bg='white',font=('URW Chancery L',20,'bold'),text='Welcome to G Worlds,..').grid(row=1,column=1,columnspan=3)
   Button(root,padx=16,bd=8,fg='blue',bg='white',font=('URW Chancery L',20,'bold'),text='Back',command=root.destroy).grid(row=4,column=2)
   root.mainloop()

def upd():
   root=Tk()
   root.title('Update ')
   root.configure(background='white')
   Label(root,padx=16,bd=8,fg="blue",bg='white',font=('URW Chancery L',20,'bold'),text='Your G editor 2k is up to date,..').grid(row=1,column=1,columnspan=3)
   Button(root,padx=16,bd=8,fg='blue',bg='white',font=('URW Chancery L',20,'bold'),text='Back',command=root.destroy).grid(row=4,column=2)
   root.mainloop()

def ver():
   root=Tk()
   root.title('version')
   root.configure(background='white')
   Label(root,padx=16,bd=8,fg="blue",bg='white',font=('URW Chancery L',20,'bold'),text='Your are using G editor 2k version 1.2.5 ,..').grid(row=1,column=1,columnspan=3,rowspan=2)
   Button(root,padx=16,bd=8,fg='blue',bg='white',font=('URW Chancery L',20,'bold'),text='Back',command=root.destroy).grid(row=4,column=2)
   root.mainloop()


aboutmenu=Menu(amenu)
fmenu.add_cascade(label='About',menu=aboutmenu)
aboutmenu.add_command(label='About us',command=aus)
aboutmenu.add_command(label='Updates ',command=upd)
aboutmenu.add_command(label='Version',command=ver)

rt.mainloop()
