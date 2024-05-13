import tkinter as tk
from tkinter import ttk
from constants import *
from tkcalendar import *
from database import DatabaseService
from PIL import ImageTk, Image


def main():
    db = DatabaseService()
    db.initilize()
    root = tk.Tk()

    """SETTINGS"""

    # initial screen settings
    root.geometry("800x250")
    root.resizable(False, False)
    root.title("Navire")
    root.configure(background="white")

    # Create header frame
    header = tk.Frame(root, background="white")
    header.pack(side=tk.TOP)

    # Create body frame
    body = tk.Frame(root, background="white")
    body.pack(side=tk.TOP)

    """HEADER"""

    # header text
    img = Image.open("assets/republic_of_algeria_image.jpg")
    resized_image = img.resize((650, 80))
    new_image = ImageTk.PhotoImage(resized_image)
    panel = tk.Label(header, image=new_image)
    panel.grid(row=1, column=1)

    """BODY"""
    # --------------- Owner --------------- #
    # ship owner text
    ship_owner_label: tk.Label = tk.Label(
        master=body, font=("Arial", 15), text="Propriétaire", background="white"
    )
    ship_owner_label.grid(row=1, column=1)
    # ship owner text field
    ship_owner_text_field: tk.Text = tk.Text(
        body,
        height=1,
        width=20,
        font=("Arial", 15),
        background="#f2f2f2",
    )
    ship_owner_text_field.grid(row=1, column=2)
    # --------------- Type --------------- #
    # ship type text
    ship_type_label: tk.Label = tk.Label(
        master=body, font=("Arial", 15), text="Type", background="white"
    )
    ship_type_label.grid(row=1, column=3)
    # ship type menu.
    ship_type_options: list = ship_types
    ship_type_dropdown_var: tk.StringVar = tk.StringVar(root)
    ship_type_dropdown_var.set(ship_type_options[0])  # Default value
    ship_type_menu: tk.OptionMenu = ttk.Combobox(
        master=body,
        textvariable=ship_type_dropdown_var,
        values=ship_type_options,
        font=("Arial", 16),
    )
    ship_type_menu.config(width=17)
    ship_type_menu.grid(row=1, column=4)
    # --------------- Geometry --------------- #
    # geometry height text
    geometry_height: tk.Label = tk.Label(
        master=body, font=("Arial", 15), text="Longeur", background="white"
    )
    geometry_height.grid(row=2, column=1)
    # geometry height text field
    geometry_height_text_field: tk.Text = tk.Text(
        body,
        height=1,
        width=20,
        font=("Arial", 15),
        background="#f2f2f2",
    )
    geometry_height_text_field.grid(row=2, column=2)
    # geometry width text
    geometry_width: tk.Label = tk.Label(
        master=body, font=("Arial", 15), text="Largeur", background="white"
    )
    geometry_width.grid(row=2, column=3)
    # geometry width text field
    geometry_width_text_field: tk.Text = tk.Text(
        body,
        height=1,
        width=20,
        font=("Arial", 15),
        background="#f2f2f2",
    )
    geometry_width_text_field.grid(row=2, column=4)

    # --------------- Charge --------------- #
    # Charge text
    charge_text: tk.Label = tk.Label(
        master=body, font=("Arial", 15), text="Charge", background="white"
    )
    charge_text.grid(row=3, column=1)
    # charge text field
    charge_text_field: tk.Text = tk.Text(
        body,
        height=1,
        width=20,
        font=("Arial", 15),
        background="#f2f2f2",
    )
    charge_text_field.grid(row=3, column=2)

    # --------------- Propultion --------------- #
    # propultion type text
    propultion_type_label: tk.Label = tk.Label(
        master=body, font=("Arial", 15), text="Propultion", background="white"
    )
    propultion_type_label.grid(row=3, column=3)
    # propultion type menu
    propultion_type_options: list = propultion_types
    propultion_type_dropdown_var: tk.StringVar = tk.StringVar(root)
    propultion_type_dropdown_var.set(propultion_type_options[0])  # Default value
    propultion_type_menu: tk.OptionMenu = ttk.Combobox(
        master=body,
        values=propultion_type_options,
        textvariable=propultion_type_dropdown_var,
        font=("Arial", 16),
    )

    # Set the background color using style
    style = ttk.Style()
    style.theme_use("clam")  # Use a theme to access style settings
    style.configure("TCombobox", fieldbackground="#f2f2f2")  # Set background color
    propultion_type_menu.config(width=17)
    propultion_type_menu.grid(row=3, column=4)
    # ---------------  Initiale date --------------- #
    # initiale date text
    initiale_date_text: tk.Label = tk.Label(
        master=body, font=("Arial", 15), text="Mise en eau", background="white"
    )
    initiale_date_text.grid(row=4, column=1)

    # initiale date calendar
    initiale_date_cal = DateEntry(
        master=body,
        width=17,
        background="darkblue",
        foreground="white",
        borderwidth=2,
        font=("Arial", 16),
    )
    initiale_date_cal.grid(row=4, column=2)
    # ---------------  Generate button --------------- #
    generate_button = tk.Button(
        body,
        text="Generate",
        width=20,
        command=lambda: db.register_ship(
            owner=ship_owner_text_field.get(
                index1="0.0",
                index2=tk.END,
            ),
            ship_type=ship_type_dropdown_var.get(),
            height=geometry_height_text_field.get(
                index1="0.0",
                index2=tk.END,
            ),
            width=geometry_width_text_field.get(
                index1="0.0",
                index2=tk.END,
            ),
            charge=charge_text_field.get(
                index1="0.0",
                index2=tk.END,
            ),
            propultion=propultion_type_dropdown_var.get(),
            initial_date=initiale_date_cal.get_date(),
        ),
    )
    generate_button.grid(row=5, column=3)

    # update screen
    root.update()
    # mianloop
    root.mainloop()


if __name__ == "__main__":
    main()
