from tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.maxsize(900, 700)
root.minsize(900, 700)
label = Frame(root, width=900)
label.pack()


def click():
    root.quit()



fig, ax = plt.subplots(figsize=(10, 3), subplot_kw=dict(aspect="equal"))

bar1 = FigureCanvasTkAgg(fig, root)
bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

data = [98.2, 1.2, 0.4, 0.2]
ingredients = ["C++", "Python", "Java", "Others"]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

btn = Button(label, text='Click', command=click)
btn.pack()

root.mainloop()

from retrying import retry
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
#
#
# data = [98.2, 1.2, 0.4, 0.2]
# ingredients = ["C++", "Python", "Java", "Others"]
#
#
# def func(pct, allvals):
#     absolute = int(np.round(pct/100.*np.sum(allvals)))
#     return "{:.1f}%\n({:d} g)".format(pct, absolute)
#
#
# wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
#                                   textprops=dict(color="w"))
#
# ax.legend(wedges, ingredients,
#           title="Ingredients",
#           loc="center left",
#           bbox_to_anchor=(1, 0, 0.5, 1))
#
# plt.setp(autotexts, size=8, weight="bold")
#
# ax.set_title("Matplotlib bakery: A pie")
#
# plt.show()