from Tkinter import *

root = Tk()
root.title("Pisarze i poeci")

var = IntVar

for poet, row, col, status in [('Ernest Hemi',0 ,0, NORMAL), \
                               ('Konrad Korzeniowski', 0, 1, NORMAL),
                               ('Cyprian Norwid', 1, 0, DISABLED),
                               ('Edgar Poe', 1, 1, NORMAL),
                               ('Adam Mickiewicz', 2, 0, NORMAL),
                               ('Julian Tuwim', 2, 1, NORMAL)]:
    setattr(var,poet,IntVar())
    Checkbutton(root, text=poet, state=status, anchor=W,
                variable=getattr(var,poet)).grid(row=row, column=col,sticky=W)

root.geometry("300x80")
root.mainloop()
print getattr(var, 'Ernest Hemi').get()