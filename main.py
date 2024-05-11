from tkinter import *
from ship import *
from tkcalendar import *
from database import Database


def main():
    root = Tk()

    """SETTINGS"""

    # initial screen settings
    root.geometry("800x250")
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
    # --------------- Owner --------------- #
    # ship owner text
    ship_owner_label: Label = Label(
        master=body, font=("Arial", 15), text="propriétaire"
    )
    ship_owner_label.grid(row=1, column=1)
    # ship owner text field
    ship_id_text_field: Text = Text(body, height=1, width=20)
    ship_id_text_field.grid(row=1, column=2)
    # --------------- Type --------------- #
    # ship type text
    ship_type_label: Label = Label(master=body, font=("Arial", 15), text="type")
    ship_type_label.grid(row=1, column=3)
    # ship type menu
    ship_type_options: list = Ship.getTypes()
    ship_type_dropdown_var: StringVar = StringVar(root)
    ship_type_dropdown_var.set(ship_type_options[0])  # Default value
    ship_type_menu: OptionMenu = OptionMenu(
        body, ship_type_dropdown_var, *ship_type_options
    )
    ship_type_menu.config(width=20)
    ship_type_menu.grid(row=1, column=4)
    # --------------- Geometry --------------- #
    # geometry height text
    geometry_height: Label = Label(master=body, font=("Arial", 15), text="longeure")
    geometry_height.grid(row=2, column=1)
    # geometry height text field
    geometry_height_text_field: Text = Text(body, height=1, width=20)
    geometry_height_text_field.grid(row=2, column=2)
    # geometry width text
    geometry_width: Label = Label(master=body, font=("Arial", 15), text="largeure")
    geometry_width.grid(row=2, column=3)
    # geometry width text field
    geometry_width_text_field: Text = Text(body, height=1, width=20)
    geometry_width_text_field.grid(row=2, column=4)

    # --------------- Charge --------------- #
    # Charge text
    charge_text: Label = Label(master=body, font=("Arial", 15), text="Charge")
    charge_text.grid(row=3, column=1)
    # charge text field
    charge_text_field: Text = Text(body, height=1, width=20)
    charge_text_field.grid(row=3, column=2)

    # --------------- Propultion --------------- #
    # propultion type text
    propultion_type_label: Label = Label(
        master=body, font=("Arial", 15), text="propultion"
    )
    propultion_type_label.grid(row=3, column=3)
    # propultion type menu
    propultion_type_options: list = Ship.getPropultion()
    propultion_type_dropdown_var: StringVar = StringVar(root)
    propultion_type_dropdown_var.set(propultion_type_options[0])  # Default value
    ship_type_menu: OptionMenu = OptionMenu(
        body, propultion_type_dropdown_var, *propultion_type_options
    )
    ship_type_menu.config(width=20)
    ship_type_menu.grid(row=3, column=4)
    # ---------------  Initiale date --------------- #
    # initiale date text
    initiale_date_text: Label = Label(master=body, font=("Arial", 15), text="initiale date")
    initiale_date_text.grid(row=4,column=1)

    # initiale date calendar
    initiale_date__cal = DateEntry(
        body, width=24, background="darkblue", foreground="white", borderwidth=2, 
    )
    initiale_date__cal.grid(row=4, column=2)
        # ---------------  Generate button --------------- #
    generate_button = Button(body,text="Generate",width=20)
    generate_button.grid(row=5,column=3)

    # update screen
    root.update()
    # mianloop
    root.mainloop()


if __name__ == "__main__":
    main()
