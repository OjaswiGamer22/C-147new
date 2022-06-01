from tkinter import *
root=Tk()
root.title("ASCII")
root.geometry("500x500")
root.configure(background="grey")
input_box=Entry(root)
input_box.place(relx=0.5,rely=0.4,anchor=CENTER)
label1=Label(root, text="Name an ascii",bg="yellow")
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
label2=Label(root, text="Encrypted Name",bg="yellow")
label2.place(relx=0.5,rely=0.7,anchor=CENTER)
def show_ascii():
    input_name=input_box.get()
    for letter in input_name:
        label1["text"]+=str(ord(letter))+" "
        ascii=int(ord(letter))
        encrypted=ascii-1
        label2["text"]+=str(chr(encrypted))
button1=Button(root,text="show name in ascii", command=show_ascii)

button1.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
