"""v0.12"""

import os
import sys

master_path = os.path.dirname(__file__)
sys.path.append(master_path)

import tkinter as tk
from PIL import Image, ImageTk

import player as pg

from language_dictionary import *

global tk_image


class InterfaceMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class InterfaceSingleton(metaclass=InterfaceMeta):
    def __init__(self):
        # creazione della finestra di gioco
        self.window = tk.Tk()
        self.window.configure(bg='black')
        self.window.title("Necrotic Dominion v0.12")
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        # self.window.iconbitmap("./media/ic.ico")

        self.lang = "it"

        # Create the textbox over the image
        self.text_box_over_image = tk.Text(self.window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                                    highlightbackground='black', borderwidth=0)
        self.text_box_over_image.place(x=0, y=0, width=800, height=30)

        # Create the textbox on the right
        self.text_box_right = tk.Text(self.window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                                highlightbackground='black', borderwidth=0)
        self.text_box_right.place(x=525, y=30, width=275, height=512)

        self.text_box_bottom = tk.Text(self.window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                                highlightbackground='black', borderwidth=0)
        self.text_box_bottom.place(x=0, y=541, width=800, height=30)

        self.text_box_vertical = tk.Text(self.window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                                    highlightbackground='black', borderwidth=0)
        self.text_box_vertical.place(x=512, y=30, width=13, height=515)

        # creazione del frame per i bottoni
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(side="bottom", fill=tk.X)


    def show_text(self, text):
        """Visualizza il testo nella finestra di gioco."""

        # Define colors for the placeholders
        vita_color = '#00e600'
        forza_color = '#ff1a1a'
        mana_color = '#3399ff'
        oro_color = '#ffd633'

        # Update the textbox over the image
        self.text_box_over_image.config(state=tk.NORMAL)
        self.text_box_over_image.delete("1.0", tk.END)

        # Use tags to set colors for the placeholders
        self.text_box_over_image.tag_config(translations["interface_life"][self.lang], foreground=vita_color)
        self.text_box_over_image.tag_config(translations["interface_strenght"][self.lang], foreground=forza_color)
        self.text_box_over_image.tag_config(translations["interface_mana"][self.lang], foreground=mana_color)
        self.text_box_over_image.tag_config(translations["interface_gold"][self.lang], foreground=oro_color)

        self.text_box_over_image.insert(tk.END, translations["interface_life"][self.lang]+": {} ".format(pg.PG.PV), translations["interface_life"][self.lang])
        self.text_box_over_image.insert(tk.END, "| ")
        self.text_box_over_image.insert(tk.END, translations["interface_strenght"][self.lang]+": {} ".format(pg.PG.PF), translations["interface_strenght"][self.lang])
        self.text_box_over_image.insert(tk.END, "| ")
        self.text_box_over_image.insert(tk.END, translations["interface_mana"][self.lang]+": {} ".format(pg.PG.PM), translations["interface_mana"][self.lang])
        self.text_box_over_image.insert(tk.END, "| ")
        self.text_box_over_image.insert(tk.END, translations["interface_gold"][self.lang]+": {} ".format(pg.PG.g), translations["interface_gold"][self.lang])
        self.text_box_over_image.insert(tk.END, "|| ")
        inventory_str = '|'.join(str(item) for item in pg.PG.inventory)
        self.text_box_over_image.insert(tk.END, translations["pg_invetory"][self.lang]+": {} ".format(inventory_str))
        self.text_box_over_image.insert(tk.END, "\n----------------------------------------------------------------------------"
                                        "-----------------------")
        self.text_box_over_image.config(state=tk.DISABLED)

        # Update the textbox on the right
        self.text_box_right.config(state=tk.NORMAL)
        self.text_box_right.delete("1.0", tk.END)
        self.text_box_right.insert(tk.END, text)
        self.text_box_right.config(state=tk.DISABLED)

        self.text_box_vertical.config(state=tk.NORMAL)
        self.text_box_vertical.delete("1.0", tk.END)
        self.text_box_vertical.insert(tk.END, "||||||||||||||||||||||||||||||||")
        self.text_box_vertical.config(state=tk.DISABLED)

        self.text_box_bottom.config(state=tk.NORMAL)
        self.text_box_bottom.delete("1.0", tk.END)
        self.text_box_bottom.insert(tk.END, "-----------------------------------------------------------------------------------"
                                    "-----------------")
        self.text_box_bottom.config(state=tk.DISABLED)

    def create_buttons(self, actions):
        self.clear_buttons()
        for action in actions:  
            if action:
                button = tk.Button(self.button_frame, text=action["text"], command=action["callback"], bg='black', fg='white', bd=10,
                                highlightthickness=0, activebackground='grey')
                button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def image_wand(self, token):
        # Create the image label
        image_path = os.path.join(master_path, token + ".png")
        image = Image.open(image_path)
        resized_image = image.resize((512, 512), Image.NEAREST)  # Resize the image without antialiasing
        global tk_image  # Declare tk_image as a global variable
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(self.window, image=tk_image)
        image_label.place(x=0, y=32, width=512, height=512)


i = InterfaceSingleton()
