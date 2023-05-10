"""v0.12"""

import tkinter as tk
from PIL import Image, ImageTk

import os

import player as pg

global tk_image


# creazione della finestra di gioco
window = tk.Tk()
window.configure(bg='black')
window.title("Necrotic Dominion v0.12")
window.geometry("800x600")
window.resizable(False, False)
window.iconbitmap("./media/ic.ico")


def show_text(text):
    """Visualizza il testo nella finestra di gioco."""

    # Define colors for the placeholders
    vita_color = '#00e600'
    forza_color = '#ff1a1a'
    mana_color = '#3399ff'
    oro_color = '#ffd633'

    # Update the textbox over the image
    text_box_over_image.config(state=tk.NORMAL)
    text_box_over_image.delete("1.0", tk.END)

    # Use tags to set colors for the placeholders
    text_box_over_image.tag_config("vita", foreground=vita_color)
    text_box_over_image.tag_config("forza", foreground=forza_color)
    text_box_over_image.tag_config("mana", foreground=mana_color)
    text_box_over_image.tag_config("oro", foreground=oro_color)

    text_box_over_image.insert(tk.END, "Vita: {} ".format(pg.PG.PV), "vita")
    text_box_over_image.insert(tk.END, "| ")
    text_box_over_image.insert(tk.END, "Forza: {} ".format(pg.PG.PF), "forza")
    text_box_over_image.insert(tk.END, "| ")
    text_box_over_image.insert(tk.END, "Mana: {} ".format(pg.PG.PM), "mana")
    text_box_over_image.insert(tk.END, "| ")
    text_box_over_image.insert(tk.END, "Oro: {} ".format(pg.PG.g), "oro")
    text_box_over_image.insert(tk.END, "|| ")
    inventory_str = '|'.join(str(item) for item in pg.PG.inventory)
    text_box_over_image.insert(tk.END, "Inventario: {}".format(inventory_str))
    text_box_over_image.insert(tk.END, "\n----------------------------------------------------------------------------"
                                       "-----------------------")
    text_box_over_image.config(state=tk.DISABLED)

    # Update the textbox on the right
    text_box_right.config(state=tk.NORMAL)
    text_box_right.delete("1.0", tk.END)
    text_box_right.insert(tk.END, text)
    text_box_right.config(state=tk.DISABLED)

    text_box_vertical.config(state=tk.NORMAL)
    text_box_vertical.delete("1.0", tk.END)
    text_box_vertical.insert(tk.END, "||||||||||||||||||||||||||||||||")
    text_box_vertical.config(state=tk.DISABLED)

    text_box_bottom.config(state=tk.NORMAL)
    text_box_bottom.delete("1.0", tk.END)
    text_box_bottom.insert(tk.END, "-----------------------------------------------------------------------------------"
                                   "-----------------")
    text_box_bottom.config(state=tk.DISABLED)


def create_buttons(actions, frame):
    clear_buttons(frame)
    for action in actions:
        button = tk.Button(frame, text=action["text"], command=action["callback"], bg='black', fg='white', bd=10,
                           highlightthickness=0, activebackground='grey')
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def clear_buttons(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Create the textbox over the image
text_box_over_image = tk.Text(window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                              highlightbackground='black', borderwidth=0)
text_box_over_image.place(x=0, y=0, width=800, height=30)

# Create the textbox on the right
text_box_right = tk.Text(window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                         highlightbackground='black', borderwidth=0)
text_box_right.place(x=525, y=30, width=275, height=512)

text_box_bottom = tk.Text(window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                          highlightbackground='black', borderwidth=0)
text_box_bottom.place(x=0, y=541, width=800, height=30)

text_box_vertical = tk.Text(window, bg='black', fg='white', state=tk.DISABLED, highlightthickness=0,
                            highlightbackground='black', borderwidth=0)
text_box_vertical.place(x=512, y=30, width=13, height=515)

# creazione del frame per i bottoni
button_frame = tk.Frame(window)
button_frame.pack(side="bottom", fill=tk.X)


def image_wand(token):
    # Create the image label
    image_path = os.path.join(os.getcwd(), token + ".png")
    image = Image.open(image_path)
    resized_image = image.resize((512, 512), Image.NEAREST)  # Resize the image without antialiasing
    global tk_image  # Declare tk_image as a global variable
    tk_image = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(window, image=tk_image)
    image_label.place(x=0, y=32, width=512, height=512)


def new_play():
    image_wand("./media/start_screen")
    show_text("                                   " +
              "---------------------------------  " +
              "----------- Necrotic ------------  " +
              "---------               ---------  " +
              "----------- Dominion ------------  " +
              "---------------------------------  " +
              "                                   " +
              "                                   " +
              "                                   " +
              "           |  v0.12  |             " +
              "                                   ")
    create_buttons(start_game_actions(), button_frame)
    window.mainloop()


def start_game_actions():
    """Restituisce le azioni possibili nella schermata di inizio gioco."""
    actions = [
        {"text": "Selezione della classe", "callback": class_caller},
        {"text": "Chiudi il gioco", "callback": end_game}
    ]
    return actions


def class_caller():
    create_buttons(class_actions(), button_frame)


def class_actions():
    actions = [
        {"text": "Abile nel combattimento", "callback": pg.warrior},
        {"text": "Abile nelle arti arcane", "callback": pg.mage}
    ]
    return actions


def end_game():
    window.destroy()

