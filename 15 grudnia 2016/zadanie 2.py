from Tkinter import *

root=Tk()
root.title(u"Przyklad Canvas")

canvas = Canvas(root, width=400, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(100, 100, 200, 200)
canvas.create_line(100, 200, 200, 300)
for i in range(1, 20, 2):
    canvas.create_line(i, 0, i, 50)
canvas.create_oval(10, 10, 300, 300, width=2, fill='yellow')
canvas.create_arc(100, 200, 300, 100, fill='green')
canvas.create_rectangle(50, 200, 300, 300, width=5, fill='#8f8fff')
canvas.create_line(600, 300, 150, 150, width=10, fill='red')
photo=PhotoImage(file='lol.png')
canvas.create_image(50, 300, image=photo, anchor=NW)
widget=Label(canvas, text=u'Kolo', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)
canvas.create_text(100, 280, text=u'Prostokat')
root.mainloop()