#!/usr/bin/python3
from tkinter import *
import math
	
class Sample(Tk):
	def __init__(self,*args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		container = Frame(self)
		container.pack(side="top", fill="both", expand = True)
		#container.grid(row=0, column=0, sticky="nsew")
		self.frames = {}
		self.container=container
		#for F in (PageOne, PageTwo):
			#page_name=F.__name__
		frame=PageOne(self.container, self)
		self.frames[PageOne]=frame
		frame_=PageTwo(self.container, self)
		self.frames[PageTwo] = frame_
		frame1=PageThree(self.container, self)
		self.frames[PageThree] = frame1
		frame2=PageFour(self.container, self)
		self.frames[PageFour] = frame2
			#frame.grid(row=0, column=0, sticky="nsew")
		frame.pack(side="top", fill="both", expand=True)

		#frame_.pack(side="top", fill="both", expand=True)
		self.show_frame(PageOne)

	def show_frame(self, page):
		frame = self.frames[page]

		frame.pack(side="top", fill="both", expand=True)
		frame.tkraise()

	def quitAll(self):
		Tk.destroy(self)
	
class PageOne(Frame):

	def __init__(self,parent,controller):
		Frame.__init__(self,parent)
		self.parent = parent
		self.controller=controller
		self.label = Label(self, text="Welcome!")
		self.label.pack()
		Button(self, text="Next", command=lambda:self.closeCur(controller)).pack()
		pass
	
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageTwo)

class PageTwo(Frame):

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller=controller		
		Label(self, text="Calculator").pack()
		Button(self, text="Next", command=lambda:self.closeCur(controller)).pack()

		display = StringVar()
		Entry(self, relief=SUNKEN, 
			textvariable=display).pack(side=TOP, expand=YES, 
			fill=BOTH)

		for key in ("123", "456", "789", "-0."):
			keyF = self.frame(TOP)
			for char in key:
				self.button(keyF, LEFT, char,
					   lambda w=display, c=char: w.set(w.get() + c))
		opsF = self.frame(TOP)
		for char in "+-*/=":
			if char == '=':
				btn = self.button(opsF, LEFT, char)
				btn.bind('<ButtonRelease-1>',
						 lambda e, s=self, w=display: s.calc(w), '+')
			else:
				btn = self.button(opsF, LEFT, char,
				   lambda w=display, s=' %s '%char: w.set(w.get()+s))

		clearF = self.frame(BOTTOM)
		self.button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))

	def button(self, btn, side, text, command=None): 
		w = Button(btn, text=text, command=command) 
		w.pack(side=side, expand=YES, fill=BOTH)
		return w
	def frame(self, side): 
		w = Frame(self)
		w.pack(side=side, expand=YES, fill=BOTH)
		return w

	def calc(self, display):
		try:
			display.set(eval(display.get()))
		except:
			display.set("ERROR")
	
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageThree)

	
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageThree)

class PageThree(Frame):
	def __init__(self,parent,controller):

		Frame.__init__(self, parent)
		self.controller=controller
		Label(self, text="Feedback").pack()
		Button(self, text="Next", command=lambda:self.closeCur(controller)).pack()
	        Label(self, text="First Name:").pack(padx=10)#grid(row=0,column=1)
        	self.nf = Entry(self).pack(padx=10)#grid(row=0,column=2,columnspan=6)
        	Label(self, text="Second Name:").pack(padx=10)#grid(row=1,column=1)
        	self.ns = Entry(self).pack(padx=10)#grid(row=1,column=2,columnspan=6)
        
        	val=IntVar()
		val.set(0)
		Label(self, text="Rate your experience").pack()
		rating = [("Excellent",1),
				("V.Good",2),
				("Good",3),
				("Okay",4),
				("V.Bad",5)]
		for v,r in enumerate(rating):
			Radiobutton(self, 
				text=r,
				padx = 20, 
				variable=val, 
				command=lambda:self.ShowChoice(val),
				value=v).pack(anchor=W)

	        var=StringVar(self)
		var.set("choose")
	        Label(self, text="Profession: ").pack(padx=10)
        	prof=["Editor","Student","Dev","HR"]
        	obj= OptionMenu(self,var,*prof)
        	obj.pack()
      
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageFour)

	def ShowChoice(self,val):
		print(val.get())


class PageFour(Frame):
	def __init__(self,parent,controller):

		Frame.__init__(self, parent)
		self.controller=controller
		Label(self, text="Thank you, you may exit").pack()
		Button(self, text="Quit", command=lambda:self.closeAll(controller)).pack()

	def closeAll(self,controller):
		#self.pack_forget()
		controller.quitAll()


#root = Tk()		
app = Sample()
app.geometry("500x500+500+500")
app.mainloop()
