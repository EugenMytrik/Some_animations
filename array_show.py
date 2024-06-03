from tkinter import *

array_a = [[1 if i == j or i == 4 - j else 0 for j in range(5)] for i in range(5)]

array_b = [[1 for j in range(5)] for i in range(5)]
for i in range(1, 4):
    for j in range(1, 4):
        array_b[i][j] = 0

array_v = [[0 for j in range(6)] for i in range(6)]
for i in range(6):
    for j in range(6):
        if abs(i - 5) > i:
            if i <= j <= abs(i - 5):
                array_v[i][j] = i + 1
        else:
            if abs(i - 5) <= j <= i:
                array_v[i][j] = i + 1

array_g = [[2 ** (i + j + 1) if i != 0 else 2 for j in range(7)] for i in range(7)]

array_d = [
    [1 if abs(i - 2) + abs(j - 2) <= 2 else 0 for j in range(5)] for i in range(5)
]

root = Tk()
root.title("Mytrik")


def display_array(array, x0, y0):
    rows = len(array)
    cols = len(array[0])
    for i in range(rows):
        for j in range(cols):
            color = "green" if array[i][j] != 0 else "white"
            label = Label(
                root,
                text=str(array[i][j]),
                width=5,
                height=2,
                bg=color,
                fg="black",
                relief="solid",
            )
            label.place(x=x0 + 40 * j, y=y0 + 30 * i)


display_array(array_a, 10, 10)
display_array(array_b, 250, 10)
display_array(array_v, 500, 10)
display_array(array_g, 10, 200)
display_array(array_d, 10, 450)
root.mainloop()
