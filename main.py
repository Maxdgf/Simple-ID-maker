from tkinter import *
from random import randint
from tkinter import messagebox

root = Tk()
root.title("ID maker")
root.geometry("500x500")
root.configure(bg="green")


def exitRoot():
    root.destroy()


def generateID():
    try:
        num1 = int(count1.get())
        num2 = int(count2.get())
        txt = "ID"
        resultID = randint(num1, num2)
        result = txt + str(resultID)
        answer.insert(0, result)
    except:
        messagebox.showerror("ERROR", "Number range is null!")


#def copyID():
    #selected_content = answer.get(answer.curselection())
    #root.clipboard_clear()
    #root.clipboard_append(selected_content)

Label(text="ID maker", font=("Verdana", 30)).pack(pady=50)
Label(text="Number range:").pack(pady=10)
count1 = Entry(width=40)
count1.pack(pady=10)
count2 = Entry(width=40)
count2.pack(pady=10)
Label(text="Result:").pack(pady=10)
answer = Listbox(width=50, height=1)
answer.pack()
Button(text="Generate ID", bg="yellow", command=generateID).pack(pady=20)
#Label(text="Copy ID:").pack(pady=20)
#Button(text="Copy ID", bg="orange", width=20, command=copyID).pack()
Button(text="exit", bg="red", width=3, command=exitRoot).place(x=0, y=0)

root.mainloop()
