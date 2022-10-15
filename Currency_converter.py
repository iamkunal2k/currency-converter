from tkinter import *
from tkinter import ttk


converter = Tk()
converter.title("Currency Converter")
converter.geometry("600x420")

OPTIONS = {
    "Australian Dollar":0.019,
    "Brazilian Real":0.075,
    "Pound Sterling":0.010,
    "Chinese Yuan":0.085,
    "Euro":0.012,
    "HongKong Dollar":0.10,
    "Indonesian Rupiah":191.87,
    "Japanese Yen":1.50,
    "Pakistani Rupee":2.35,
    "SriLankan Rupee":2.69,
    "Swiss Franc":0.012,
    "Us Dollar":0.013
        }



def ok():
    price = rupees.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ",INSERT,converted)

bg = PhotoImage(file="abcx.png")
Label1 = Label(converter, image=bg)
Label1.place(x=0,y=0)

appName = Label(converter,text="Currency Converter",font=("Colonna MT",28,"bold","underline"),fg="dark green")
appName.place(x=130, y=10)


result = Text(converter,height=5,width=50,font=("Cambria",10,"bold"),bd=5)
result.place(x=80, y=60)

india = Label(converter,text="Value in Indian Rupees:",font=("Cambria",12,"bold"),fg="red")
india.place(x=50, y=165)

rupees = Entry(converter,font=("Cambria",20))
rupees.place(x=220, y=160)

choice = Label(converter,text="Choice:",font=("Cambria",14,"bold"),fg="orange")
choice.place(x=50, y=214)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter,variable1,*OPTIONS)
option.place(x=120 , y=210, width=150, height=40)

button = Button(converter,text="Convert",fg="green",font=("arial",20),bg="powder blue",command=ok)
button.place(x=350, y=210,height=40,width=150)

converter.mainloop()