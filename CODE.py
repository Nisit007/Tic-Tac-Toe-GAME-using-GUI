# CDOE BY NISHIT PATEL

from tkinter import *
import tkinter
from tkinter.messagebox import showinfo
window = tkinter.Tk()
window.title("Tic-tac-toe")

y = ""
x = 2

player_1 = []
player_2 = []


def define_sign(number):
    global x, y
    global player_1, player_2

    from itertools import permutations
    set1 = permutations([1, 2, 3])
    set2 = permutations([3, 5, 7])
    set3 = permutations([1, 5, 9])
    set4 = permutations([4, 5, 6])
    set5 = permutations([7, 8, 9])
    set6 = permutations([1, 4, 7])
    set7 = permutations([2, 5, 8])
    set8 = permutations([3, 6, 9])

    for i in set1, set2, set3, set4, set5, set6, set7, set8:
        for j in list(i):
            plyr_1 = all(elem in player_1 for elem in j)
            plyr_2 = all(elem in player_2 for elem in j)
            if plyr_1 == True:
                print("Player 1 wins")
                showinfo("Game Result", "Player 1 Won")
                break
            elif plyr_2 == True:
                print("Plater 2 wins")
                showinfo("Game Result", "Player 2 Won")
                break
            else:
                pass
    if number == 1:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn1.config(text=y)
        x = x + 1
    if number == 2:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn2.config(text=y)
        x = x + 1

    if number == 3:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn3.config(text=y)
        x = x + 1

    if number == 4:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn4.config(text=y)
        x = x + 1

    if number == 5:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn5.config(text=y)
        x = x + 1

    if number == 6:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn6.config(text=y)
        x = x + 1

    if number == 7:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn7.config(text=y)
        x = x + 1

    if number == 8:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn8.config(text=y)
        x = x + 1

    if number == 9:
        if x % 2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x % 2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        btn9.config(text=y)
        x = x + 1




lbl1 = Label(window, text="Player 1 : x", font="times 15", bg="black", fg="red")
lbl1.grid(row=0, column=1)

lbl1 = Label(window, text="Player 2 : y", font="times 15", bg="black", fg="red")
lbl1.grid(row=0, column=2)

btn1 = Button(window, width=20, height=10, command=lambda: define_sign(1), bg="black", fg="white")
btn1.grid(row=1, column=1)
btn2 = Button(window, width=20, height=10, command=lambda: define_sign(2), bg="black", fg="white")
btn2.grid(row=1, column=2)
btn3 = Button(window, width=20, height=10, command=lambda: define_sign(3), bg="black", fg="white")
btn3.grid(row=1, column=3)
btn4 = Button(window, width=20, height=10, command=lambda: define_sign(4), bg="black", fg="white")
btn4.grid(row=4, column=1)
btn5 = Button(window, width=20, height=10, command=lambda: define_sign(5), bg="black", fg="white")
btn5.grid(row=4, column=2)
btn6 = Button(window, width=20, height=10, command=lambda: define_sign(6), bg="black", fg="white")
btn6.grid(row=4, column=3)
btn7 = Button(window, width=20, height=10, command=lambda: define_sign(7), bg="black", fg="white")
btn7.grid(row=8, column=1)
btn8 = Button(window, width=20, height=10, command=lambda: define_sign(8), bg="black", fg="white")
btn8.grid(row=8, column=2)
btn9 = Button(window, width=20, height=10, command=lambda: define_sign(9), bg="black", fg="white")
btn9.grid(row=8, column=3)

window.mainloop()
