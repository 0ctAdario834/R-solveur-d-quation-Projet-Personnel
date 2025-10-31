from tkinter import *  # type: ignore
from tkinter import ttk
from tabs.QdrtcTab import create_quadratic_tab
from tabs.AbsltTab import create_absolute_tab
from tabs.SqrtTab import create_sqrt_tab
from tabs.RtnlTab import create_rtnl_tab
from utils import set_format

window = Tk()
window.geometry("900x720")
window.resizable(False, False)
window.title("Résolveur d'Équations\nProjet Personnel")
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background='#676767')

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

home = Frame(notebook)
notebook.add(home,text=" | Accueil | ")
home.config(background='#999999')

create_quadratic_tab(notebook, window)
create_absolute_tab(notebook, window)
create_sqrt_tab(notebook, window)
create_rtnl_tab(notebook, window)

Result_Format = ['Fractions', 'Décimales']

format_var = StringVar(value="Decimal")

def update_output_format():
    set_format(format_var.get())
    print(f"Output format set to: {format_var.get()}")

format_frame = Frame(home,
                     relief=RAISED,
                     border=16,
                     padx=16,
                     pady=8)
format_frame.place(relx=0.4, y=20)

format_label = Label(format_frame,
                     text="Format des Résultats",
                     font=('Comic Sans MS', 12))
format_label.pack()

for index, format_option in enumerate(Result_Format):
    radiobutton = Radiobutton(format_frame,
                     text=format_option,
                     variable=format_var,
                     value=format_option,
                     command=update_output_format,
                     font=('Comic Sans MS', 12))
    radiobutton.pack()

HelloLabel = Label(home,
                   text="Résolveur d'Équations\n\nCréé par: Adam Haddach\n\nSéléctionnez un onglet pour commencer.",
                   bg='#eeeeee',
                   font=('Comic Sans MS', 24),
                   relief=RAISED,
                   border=32,
                   padx=16,
                   pady=16,
                   justify=CENTER,
                   highlightbackground='#444444',
                   highlightcolor='#888888',
                   highlightthickness=4)
HelloLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
