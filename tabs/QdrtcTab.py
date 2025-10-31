from tkinter import * # type: ignore
from tkinter import ttk
from tkinter import messagebox
import math
import cmath
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fractions import Fraction
from utils import get_format

def create_quadratic_tab(notebook, window):
    tab_qdrtceqnslvr = Frame(notebook)
    notebook.add(tab_qdrtceqnslvr,text=" | Équation Quadratique | ")
    tab_qdrtceqnslvr.config(background='#999999')

    entry_accuracy = None

    name = Label(tab_qdrtceqnslvr,
                 text="Résolveur d'Équations Quadratiques",
                 font=('Comic Sans MS',36),
                 background='#ffffff',
                 relief=RAISED,
                 border=8,
                 padx=8,
                 pady=8)
    name.pack(side=TOP,pady=16)

    def add_placeholder(entry_widget, placeholder):
        def on_focus_in(event):
            if entry_widget.get() == placeholder:
                entry_widget.delete(0, "end")
                entry_widget.config(fg="black")
        def on_focus_out(event):
            if entry_widget.get() == "":
                entry_widget.insert(0, placeholder)
                entry_widget.config(fg="gray")
        entry_widget.insert(0, placeholder)
        entry_widget.config(fg="gray")
        entry_widget.bind("<FocusIn>", on_focus_in)
        entry_widget.bind("<FocusOut>", on_focus_out)

    accuracy_frame = Frame(tab_qdrtceqnslvr, bg="#999999", relief=RAISED, border=16, padx=16, pady=8)
    accuracy_frame.pack(pady=5)
    accuracy_indication = Label(accuracy_frame,text="Chiffres significatifs:",font=('Comic Sans MS',12),fg="#333333",relief=RAISED,border=4,width=16)
    accuracy_indication.pack(side=LEFT,padx=4)
    entry_accuracy = Entry(accuracy_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_accuracy.pack(padx=4)
    add_placeholder(entry_accuracy, "décimales...")

    coeff_frame = Frame(tab_qdrtceqnslvr, bg="#999999", relief=RAISED, border=16, padx=16, pady=8)
    coeff_frame.pack(pady=10)

    expected_eqn_frame = Frame(coeff_frame, bg="#ffffff", relief=RAISED, border=8, padx=8, pady=4)
    expected_eqn_frame.pack(side=TOP, pady=4)
    def expected_eqn():
        fig, ax = plt.subplots(figsize=(2, 0.5), dpi=100)
        ax.axis('off')
        ax.text(0.5, 0.5, r"$y = ax² + bx + c$", fontsize=12, ha='center', va='center')
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        return fig
    canvas = FigureCanvasTkAgg(expected_eqn(), master=expected_eqn_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    entry_a = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_a.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_a, "Valeur a...")

    entry_b = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_b.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_b, "Valeur b...")

    entry_c = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_c.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_c, "Valeur c...")

    entry_y = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_y.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_y, "Valeur y...")

    def SolveQdrtcEquation():
        try:
            a_raw = entry_a.get()
            b_raw = entry_b.get()
            c_raw = entry_c.get()
            y_raw = entry_y.get()
            a = float(-1 if a_raw.strip() == "-" else a_raw if a_raw != "Valeur a..." else 1)
            b = float(-1 if b_raw.strip() == "-" else b_raw if b_raw != "Valeur b..." else 0)
            c = float(c_raw if c_raw != "Valeur c..." else 0)
            y = float(y_raw if y_raw != "Valeur y..." else 0)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")
            return
        accuracy = None
        try:
            if entry_accuracy is not None:
                raw = entry_accuracy.get()
                if raw not in ('', "décimales..."):
                    parsed = int(raw)
                    if parsed >= 0:
                        accuracy = parsed
        except ValueError:
            accuracy = None
        try:
            if a == 0:
                messagebox.showerror("Erreur", "Ceci n'est pas une équation quadratique.")
                return
            printa = 'x²' if a == 1 else '-x²' if a == -1 else f'{a}x²'
            printb = '' if b == 0 else f"+ {abs(b)}x" if b > 0 else f"- {abs(b)}x"
            printc = '' if c == 0 else f"+ {abs(c)}" if c > 0 else f"- {abs(c)}"
            printy = y
            confirmfnc = messagebox.askyesno('Confirmation', f"La fonction est {printy} = {printa}{printb}{printc} ?")
            if not confirmfnc:
                return
            discriminant = b**2-4*a*(c-y)
            if discriminant < 0:
                msg = "Il n'y a pas de solutions."
                messagebox.showinfo("Résultat", msg)
                display_result(msg)
            elif discriminant == 0:
                root = -b/(2*a)
                if root == 0:
                    root = 0
                if get_format() == 'Décimales':
                    if accuracy is not None:
                        msg = f"Une solution: {root:.{accuracy}f}"
                        messagebox.showinfo("Solution", msg)
                        display_result(msg)
                    else:
                        msg = f"Une solution: {root}"
                        messagebox.showinfo("Solution", msg)
                        display_result(msg)
                elif get_format() == 'Fractions':
                    frac = Fraction(root).limit_denominator()
                    msg = f"Une solution: {frac}"
                    messagebox.showinfo("Solution", msg)
                    display_result(msg)
            else:
                root1 = (-b+math.sqrt(discriminant))/(2*a)
                root2 = (-b-math.sqrt(discriminant))/(2*a)
                if get_format() == 'Décimales':
                    if accuracy is not None:
                        msg = f"Solutions:\n{root1:.{accuracy}f}, {root2:.{accuracy}f}"
                        messagebox.showinfo("Solutions", msg)
                        display_result(msg)
                    else:
                        msg = f"Solutions:\n{root1}, {root2}"
                        messagebox.showinfo("Solutions", msg)
                        display_result(msg)
                elif get_format() == 'Fractions':
                    frac1 = Fraction(root1).limit_denominator()
                    frac2 = Fraction(root2).limit_denominator()
                    msg = f"Solutions:\n{frac1}, {frac2}"
                    messagebox.showinfo("Solutions", msg)
                    display_result(msg)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur inattendue s'est produite:\n{e}")

    solve_button = Button(tab_qdrtceqnslvr,
                          text="Résoudre l'Équation",
                          command=SolveQdrtcEquation,
                          border=8,
                          relief=RAISED,
                          padx=4,
                          pady=4)
    solve_button.pack(pady=16)

    def clear_results():
        results_box.delete("1.0", END)

    def copy_results():
        text = results_box.get("1.0", END).strip()
        if text:
            window.clipboard_clear()
            window.clipboard_append(text)
            window.update()

    buttons_frame = Frame(tab_qdrtceqnslvr, bg="#999999")
    buttons_frame.pack(pady=5)

    clear_button = Button(buttons_frame,
                          text="Effacer les Résultats",
                          command=clear_results,
                          border=8,
                          relief=RAISED,
                          padx=4,
                          pady=4)
    clear_button.pack(side=LEFT, padx=5)

    copy_button = Button(buttons_frame,
                         text="Copier les Résultats",
                         command=copy_results,
                         border=8,
                         relief=RAISED,
                         padx=4,
                         pady=4)
    copy_button.pack(side=LEFT, padx=5)

    results_frame = Frame(tab_qdrtceqnslvr, bg="#999999", relief=RAISED, border=8, padx=8, pady=8)
    results_frame.pack(pady=10, fill=X)

    results_box = Text(results_frame,
                       font=('Comic Sans MS', 12),
                       height=8, width=60,
                       wrap=WORD,
                       relief=RAISED, border=4)
    results_box.pack(side=LEFT, fill=BOTH, expand=True)

    def display_result(text):
        results_box.insert(END, text + "\n")
        results_box.see(END)

    return tab_qdrtceqnslvr
