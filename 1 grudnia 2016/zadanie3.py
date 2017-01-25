import Tkinter
from IPython import display


class App:
    def __init__(self, master):
        Tkinter.Button(master, text='Przycisk 1').pack(side=Tkinter.TOP)
        Tkinter.Button(master, text='Przycisk 2').pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text='Przycisk 3').pack(side=Tkinter.RIGHT)
root = Tkinter.Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title(u"Przyk\u0142ad geometrii pack ")
display = App(root)
root.mainloop()