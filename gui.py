import tkinter as tk

window = tk.Tk()

window.title('first window.')
window.geometry('500x300')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='lightgray', fg='blue', font=('Arial', 12), width=30, height=2)
l.pack()

count = 0
def hit():
  global count
  count = count + 1
  var.set(count)

b = tk.Button(window, text='hit', width=6, height=2, command=hit)
b.pack()

e1 = tk.Entry(window, show='*', font=('Arial', 14))
e2 = tk.Entry(window, show=None, font=('Arial', 14))
e1.pack()
e2.pack()

window.mainloop()
