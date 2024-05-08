from tkinter import *
from ship import *
from database import Database


def main():
    root = Tk()

    """SETTINGS"""

    # initial screen settings
    root.geometry("1000x500")
    root.resizable(False, False)

    root.title("navire")

    # Create header frame [pack]
    header = Frame(root)
    header.pack(side=TOP)

    # Create body frame [grid]
    body = Frame(root)
    body.pack(side=TOP)

    """HEADER"""

    # header text
    title_label = Label(header, font=("Arial", 30, "bold"), text="Navire ... logo")
    title_label.pack()

    """BODY"""

    # ship id text
    ship_id_label: Label = Label(master=body, font=("Arial", 15), text="ship id").grid(
        row=1, column=1
    )
    # ship id text field
    ship_id_text_field: Label = Text(body, height=1, width=20).grid(row=1, column=2)
    # ship type text
    ship_type_label: Label = Label(master=body, font=("Arial", 15), text="type").grid(
        row=2, column=1
    )
    # ship type menu
    options: list = Ship.getTypes()
    dropdown_var: StringVar = StringVar(root)
    dropdown_var.set(options[0])  # Default value
    ship_type_menu: OptionMenu = OptionMenu(body, dropdown_var, *options)
    ship_type_menu.config(width=20)
    ship_type_menu.grid(row=2, column=2)

    # update screen
    root.update()
    # mianloop
    root.mainloop()


if __name__ == "__main__":
    main()
