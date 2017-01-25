#zrob sobie choinke

from Tkinter import *

root=Tk()

canvas = Canvas(root, width=1000, height=800, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(500, 800, 500, 700, width=40, fill='brown')


for i in range (200, 700, 1):
    canvas.create_line(500, 700, 200, 740, 500, i, width=2, fill='green')

for i in range (200, 700, 1):
    canvas.create_line(500, 700, 800, 740, 500, i, width=2, fill='green')

canvas.create_oval(420, 420, 400, 400, width=0, fill='#FF33FF')
canvas.create_oval(460, 460, 440, 440, width=0, fill='#800080')
canvas.create_oval(500, 500, 480, 480, width=0, fill='YELLOW')
canvas.create_oval(540, 540, 520, 520, width=0, fill='RED')
canvas.create_oval(580, 580, 560, 560, width=0, fill='BLUE')
canvas.create_oval(620, 620, 600, 600, width=0, fill='GOLD')
canvas.create_oval(660, 660, 640, 640, width=0, fill='BROWN')
canvas.create_oval(700, 700, 680, 680, width=0, fill='#FF00FF')

#canvas.create_oval(500, 500, 480, 480, width=0, fill='#FF33FF')

root.mainloop()