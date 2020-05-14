from tkinter import *
from tkinter.messagebox import showinfo
from PIL  import Image, ImageTk
root = Tk()
root.geometry("600x500")
imge = Image.open("E:/images.jpg")
photo = ImageTk.PhotoImage(imge)
lab = Label(image=photo, bg='black')
lab.pack(fill=BOTH, expand=True)
def button():
    button1 = Button(root, text="play game", font="arial 15 bold", command=start)
    button1.place(x=30, y=380)
    button1 = Button(root, text="exit game", font="arial 15 bold", command=end)
    button1.place(x=450, y=380)

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
f8 = 0
f9 = 0
y = ''
x = 0
player_1 = []
player_2 = []

def start():

    def define_sign(number):
        global y, x, f1, f2, f3, f4, f5, f6, f7, f8, f9
        global player_1, player_2
        from itertools import permutations

        if number == 1 and f1 == 0:
            f1 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b1.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b1.config(text='O', fg="white", bg="grey")
            x = x + 1
        elif number == 2 and f2 == 0:
            f2 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b2.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b2.config(text='O', fg="white", bg="grey")
            x = x + 1
        elif number == 3 and f3 == 0:
            f3 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b3.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b3.config(text='O', fg="white", bg="grey")
            x = x + 1
        elif number == 4 and f4 == 0:
            f4 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b4.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b4.config(text='O', fg="white", bg="grey")
            x = x + 1
        elif number == 5 and f5 == 0:
            f5 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b5.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b5.config(text='O', fg="white", bg="grey")
            x = x + 1
        elif number == 6 and f6 == 0:
            f6 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b6.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b6.config(text='O',fg="white", bg="grey")
            x = x + 1
        elif number == 7 and f7 == 0:
            f7 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b7.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b7.config(text='O', fg="white", bg="grey")

            x = x + 1
        elif number == 8 and f8 == 0:
            f8 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b8.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b8.config(text='O', fg="white", bg="grey")
            x = x + 1
        elif number == 9 and f9 == 0:
            f9 = 1
            if x % 2 == 0:
                player_1.append(number)
                print(player_1)
                b9.config(text='X', fg="violet", bg="black")
            elif x % 2 != 0:
                player_2.append(number)
                print(player_2)
                b9.config(text='O', fg="white", bg="grey")
            x = x + 1

        set1 = permutations([1, 2, 3])
        set2 = permutations([4, 5, 6])
        set3 = permutations([7, 8, 9])
        set4 = permutations([1, 4, 7])
        set5 = permutations([2, 5, 8])
        set6 = permutations([3, 6, 9])
        set7 = permutations([1, 5, 9])
        set8 = permutations([3, 5, 7])

        for i in set1, set2, set3, set4, set5, set6, set7, set8:
            for j in list(i):
                plyr_1 = all(elem in player_1 for elem in j)
                plyr_2 = all(elem in player_2 for elem in j)
            if plyr_1 == True:
                print("player 1 wins")
                showinfo("game result", "player 1 has won")
                f1 = 0
                f2 = 0
                f3 = 0
                f4 = 0
                f5 = 0
                f6 = 0
                f7 = 0
                f8 = 0
                f9 = 0
                x = 0
                player_1 = []
                player_2 = []
                root.destroy()
                button()
            elif plyr_2 == True:
                print("player 2 wins")
                showinfo("game result", "player 2 has won")
                f1 = 0
                f2 = 0
                f3 = 0
                f4 = 0
                f5 = 0
                f6 = 0
                f7 = 0
                f8 = 0
                f9 = 0
                x = 0
                player_1 = []
                player_2 = []
                root.destroy()
                button()
            else:
                pass
        if plyr_1 != True and x == 9:
            print("draw")
            showinfo("game result", "draw")
            f1 = 0
            f2 = 0
            f3 = 0
            f4 = 0
            f5 = 0
            f6 = 0
            f7 = 0
            f8 = 0
            f9 = 0
            x = 0
            player_1 = []
            player_2 = []
            root.destroy()
            button()
        else:
            pass

    root = Tk()
    l1 = Label(root, text="PLAYER_1_:_X", font="arial 15 bold", fg='violet', bg='black')
    l1.grid(row=0, column=1)

    l2 = Label(root, text="PLAYER_2_:_O", font="arial 15 bold", fg='white', bg='grey')
    l2.grid(row=1, column=1)

    b1 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(1))
    b1.grid(row=2, column=2)

    b2 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(2))
    b2.grid(row=2, column=3)

    b3 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(3))
    b3.grid(row=2, column=4)

    b4 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(4))
    b4.grid(row=3, column=2)

    b5 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(5))
    b5.grid(row=3, column=3)

    b6 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(6))
    b6.grid(row=3, column=4)

    b7 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(7))
    b7.grid(row=4, column=2)

    b8 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(8))
    b8.grid(row=4, column=3)

    b9 = Button(root, text=" ", font="times 20 bold", width=15, height=5, command=lambda: define_sign(9))
    b9.grid(row=4, column=4)

def end():
    exit()

button()
root.mainloop()



