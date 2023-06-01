from tkinter import *
from tkinter import ttk


# =====> Dummy Data
data = (["ID-001", "Agosta Meghan"],
        ["ID-002", "Johnston Rebecca"],
        ["ID-003", "Stacey Laura"],
        ["ID-004", "Wakefield Jennifer"],
        ["ID-005", "Saulnier Jillian"],
        ["ID-006", "Daoust Mélodie"],
        ["ID-007", "Bram Bailey"],
        ["ID-008", "Jenner Brianne"],
        ["ID-009", "Nurse Sarah"],
        ["ID-010", "Irwin Haley"],
        ["ID-011", "Spooner Natalie"],
        ["ID-012", "Clark Emily"],
        ["ID-013", "Poulin Marie-Philip"],
        ["ID-014", "Turnbull Blayre"],
        ["ID-015", "Larocque Jocelyne"],
        ["ID-016", "Lacquette Brigette"],
        ["ID-017", "Rougeau Lauriane"],
        ["ID-018", "Fortino Laura"],
        ["ID-019", "Mikkelson Meaghan"],
        ["ID-020", "Fast Renata"],
        ["ID-021", "Szabados Shannon"],
        ["ID-022", "Lacasse Geneviève"],
        ["ID-023", "Desbiens Ann-Renée"],
        ["ID-024", "Brulé Gilbert"],
        ["ID-025", "Wolski Wojtek"],
        ["ID-026", "Roy Derek"],
        ["ID-027", "Kelly Chris"],
        ["ID-028", "Klinkhammer Rob"],
        ["ID-029", "Kozun Brandon"],
        ["ID-030", "Howden Quinton"],
        ["ID-031", "Bourque René"],
        ["ID-032", "Ebbett Andrew"],
        ["ID-033", "Raymond Mason"],
        ["ID-034", "O’Dell Eric"],
        ["ID-035", "Lapierre Maxim"],
        ["ID-036", "Vey Linden"],
        ["ID-037", "Thomas Christian"],
        ["ID-038", "Stollery Karl"],
        ["ID-039", "Lee Chris"],
        ["ID-040", "Genoway Chay"],
        ["ID-041", "Gragnani Marc-Andre"],
        ["ID-042", "Elliott Stefan"],
        ["ID-043", "Goloubef Cody"],
        ["ID-044", "Robinson Mat"],
        ["ID-045", "Noreau Maxim"],
        ["ID-046", "Scrivens Ben"],
        ["ID-047", "Poulin Kevin"],
        ["ID-048", "Peters Justin"],
        ["ID-049", "Barnes Cayla"])


# =====> Window Configuration
root = Tk()
root.title("miniFilter")
root.geometry("330x300")
root.resizable(False, False)

# =====> Functions


def load_data():
    for record in data:
        tv.insert("", END, record[0], values=(record[0], record[1]))


def apply_filter(event):
    tv.delete(*tv.get_children())
    valFilter = eVal.get()
    for record in data:
        if valFilter.lower() in record[1].lower():
            tv.insert("", END, record[0], values=(record[0], record[1]))


# =====> Variable Declaration
eVal = StringVar()

# =====> Label & Entry Field Configuration
Label(root, text="Type here --->").grid(row=0, column=0)

e1 = Entry(root, textvariable=eVal, width=30)
e1.grid(row=0, column=1)

e1.bind("<KeyRelease>", apply_filter)

# =====> Treeview Set Up as a Table and Scrollbar Set Up
f1 = Frame(root)

sb = Scrollbar(f1, orient=VERTICAL)
tv = ttk.Treeview(f1, columns=("id", "name"),
                  selectmode="browse", yscrollcommand=sb.set)
sb.config(command=tv.yview)

# -----> Columns Set Up
tv.column("#0", width=0, stretch=NO)
tv.column("id", width=80, anchor="center")
tv.column("name", width=200)

# -----> Heading Set Up
tv.heading("id", text="Id")
tv.heading("name", text="Name")

sb.pack(side=RIGHT, fill=Y)
tv.pack()
f1.grid(row=1, column=0, columnspan=2, padx=15, pady=15)

# =====> Insert Data Into Treeview
load_data()

root.mainloop()
