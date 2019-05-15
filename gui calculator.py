from tkinter import *
class calculator(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def append_display(self,text):
        self.input_text=self.display.get()
        self.length_text=len(self.input_text)

        self.display.insert(self.length_text,text)
        
    def clear_display(self,text):
        self.display.delete(0,END)
        self.display.insert(0,text)

    def result(self):
        self.expression=self.display.get()
        self.ans=eval(self.expression)
        self.clear_display(self.ans)
        
    def create_widgets(self):
        self.display=Entry(self)
        self.display.grid(row=0,column=0,columnspan=4,stick='W')

        self.b1=Button(self,text="1",command=lambda:self.append_display("1"))
        self.b1.grid(row=1,column=0,sticky='W')

        self.b2=Button(self,text="2",command=lambda:self.append_display("2"))
        self.b2.grid(row=1,column=1,sticky='W')

        self.b3=Button(self,text="3",command=lambda:self.append_display("3"))
        self.b3.grid(row=1,column=2,sticky='W')

        self.bplus=Button(self,text="+",command=lambda:self.append_display("+"))
        self.bplus.grid(row=1,column=3,sticky='W')

        self.b4=Button(self,text="4",command=lambda:self.append_display("4"))
        self.b4.grid(row=2,column=0,sticky='W')

        self.b5=Button(self,text="5",command=lambda:self.append_display("5"))
        self.b5.grid(row=2,column=1,sticky='W')

        self.b6=Button(self,text="6",command=lambda:self.append_display("6"))
        self.b6.grid(row=2,column=2,sticky='W')

        self.bminus=Button(self,text="-",command=lambda:self.append_display("-"))
        self.bminus.grid(row=2,column=3,sticky='W')

        self.b7=Button(self,text="7",command=lambda:self.append_display("7"))
        self.b7.grid(row=3,column=0,sticky='W')

        self.b8=Button(self,text="8",command=lambda:self.append_display("8"))
        self.b8.grid(row=3,column=1,sticky='W')

        self.b9=Button(self,text="9",command=lambda:self.append_display("9"))
        self.b9.grid(row=3,column=2,sticky='W')

        self.bmul=Button(self,text="*",command=lambda:self.append_display("*"))
        self.bmul.grid(row=3,column=3,sticky='W')

        self.div=Button(self,text="/",command=lambda:self.append_display("/"))
        self.div.grid(row=4,column=0,sticky='W')

        self.bclear=Button(self,text="C",command=lambda:self.clear_display(""))
        self.bclear.grid(row=4,column=1,sticky='W')

        self.bequal=Button(self,text="=",command=self.result)
        self.bequal.grid(row=4,column=2,columnspan=2,sticky='W')
        

        



root=Tk()
root.geometry("120x120")
app=calculator(root)
app.grid()
root.mainloop()
