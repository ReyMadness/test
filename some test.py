import keyboard
from tkinter import *

root = Tk()
root.title("TEST")
root.geometry("200x75")
root.resizable(False, False)

def main():
    if(keyboard.is_pressed('w')):
        W.config(fg="#00f040")
        z = Cords_z['text']
        z_new = z + 0.03
        Cords_z.config(text=z_new)
    else:
        W.config(fg="#fa0202")
    if(keyboard.is_pressed('a')):
        A.config(fg="#00f040")
        x = Cords_x['text']
        x_new = x - 0.03
        Cords_x.config(text=x_new)
    else:
        A.config(fg="#fa0202")
    if(keyboard.is_pressed('s')):
        S.config(fg="#00f040")
        z = Cords_z['text']
        z_new = z - 0.03
        Cords_z.config(text=z_new)
    else:
        S.config(fg="#fa0202")
    if(keyboard.is_pressed('d')):
        D.config(fg="#00f040")
        x = Cords_x['text']
        x_new = x + 0.03
        Cords_x.config(text=x_new)
    else:
        D.config(fg="#fa0202")
    root.after(10, main)

W = Label(text="W", fg="#fa0202")
A = Label(text="A", fg="#fa0202")
S = Label(text="S", fg="#fa0202")
D = Label(text="D", fg="#fa0202")
Cords_txt = Label(text="Your cords:")
Cords_x = Label(text=0)
Cords_x_txt = Label(text="X:")
Cords_z = Label(text=0)
Cords_z_txt = Label(text="Z:")

W.place(x=50, y=20)
A.place(x=0, y=55)
S.place(x=50, y=55)
D.place(x=100, y=55)
Cords_txt.place(x=120)
Cords_x.place(x=150, y=20)
Cords_x_txt.place(x=120, y=20)
Cords_z.place(x=150, y=40)
Cords_z_txt.place(x=120, y=40)

main()

root.mainloop()
