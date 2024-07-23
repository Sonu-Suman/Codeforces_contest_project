




# import tkinter as tk
#
# import tksheet
#
# top = tk.Tk()
#
# sheet = tksheet.Sheet(top)
#
# sheet.grid()
#
# sheet.set_sheet_data([[cj for cj in range(4)] for ri in range(6)])
#
# # table enable choices listed below:
#
# sheet.enable_bindings(("single_select",
#                        "row_select",
#                        "column_width_resize",
#                        "arrowkeys",
#                        "right_click_popup_menu",
#                        "rc_select",
#                        "rc_insert_row",
#                        "rc_delete_row",
#                        "copy",
#                        "cut",
#                        "paste",
#                        "delete",
#                        "undo",
#                        "edit_cell"))
#
# top.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import *


# ========================================================================================================================================================

root =Tk()
root.title("TreeView window")
root.iconify()
root.iconbitmap("image/apple.png")
root.geometry('500x500')

# initializing tree
my_tree = ttk.Treeview(root)

# our column
my_tree['columns'] = ("Section A", "Section B", "Section C", "Section D")

# format our columns
my_tree.column("#0", width=120, minwidth=30)
my_tree.column("Section A", anchor=W, width=120)
my_tree.column("Section B", anchor=CENTER, width=100)
my_tree.column("Section C", anchor=W, width=120)
my_tree.column("Section D", anchor=W, width=120)

# Create headings
my_tree.heading("#0", text='Label', anchor=W)
my_tree.heading("Section A", text="Section A", anchor=W)
my_tree.heading("Section B", text="Section B", anchor=CENTER)
my_tree.heading("Section C", text="Section C", anchor=W)
my_tree.heading("Section D", text="Section D", anchor=W)


my_tree['show'] = 'headings'
my_tree.pack(fill=BOTH, expand=1)

# add Data
for i in range(110):
    my_tree.insert(parent='', index='end', iid=i, text='Parent', values=("Combinator", f"binary Search{str(i)}", "Aparajita", "sortings"))

    # packing
my_tree.pack(pady=10)

# my_tree.insert(parent='', index='end', iid=110, text="Child", values=("Combinator", f"binary Search{str(i)}", "Aparajita", "sortings", 'Sonu', "Suman", "Data Str", "algorithm"))
# my_tree.insert(parent='5', index='end', iid=110, text="Child", values=("Combinator", f"binary Search{str(i)}", "Aparajita", "sortings", 'Sonu', "Suman", "Data Str", "algorithm"))
# my_tree.move('110', '5', '5')

root.mainloop()
