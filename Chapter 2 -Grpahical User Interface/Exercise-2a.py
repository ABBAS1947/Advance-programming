import tkinter as tk

root = tk.Tk()
root.title("GUI Pack Example")
root.geometry("400x200")
root.configure(bg="lightgray")

# the last few exercises of the previous chapter were hard but
# this one was such a hassle to get right.

LABEL_W = 120
LABEL_H = 40


WIN_W = 400
WIN_H = 200


label_a = tk.Label(root, text="A", bg="red", bd=5, relief="raised")
label_a.place(x=0, y=0, relwidth=1, height=LABEL_H)


label_c = tk.Label(root, text="C", bg="blue", bd=5, relief="raised")



label_d = tk.Label(root, text="D", bg="white", bd=5, relief="raised")



label_b = tk.Label(root, text="B", bg="yellow", bd=5, relief="raised")


pair_total_width = LABEL_W * 2
start_x_c = (WIN_W - pair_total_width) // 2
start_y_c = 70
start_y_b = 120


label_c.place(x=start_x_c, y=start_y_c, width=LABEL_W, height=LABEL_H)
label_b.place(x=(WIN_W - LABEL_W)//2, y=start_y_b, width=LABEL_W, height=LABEL_H)


def position_d(win_width):

    d_x = win_width - (start_x_c + LABEL_W*2)

    d_x = start_x_c + LABEL_W + (win_width - WIN_W)
    label_d.place(x=d_x, y=start_y_c, width=LABEL_W, height=LABEL_H)


position_d(WIN_W)


def on_resize(event):
    position_d(event.width)

root.bind("<Configure>", on_resize)

root.mainloop()
