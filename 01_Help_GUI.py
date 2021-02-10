from tkinter import *

from functools import partial  # To prevent unwanted windows (being created)

import random

class Converter:

    def __init__(self, parent):

        # Formatting variables...
        background_color = "purple"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)...
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "18", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (Row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "12"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:

    # Set up initial function
    def __init__(self, partner):

        background = "orange"

        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (or help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up help heading (Row 0)
        self.how_heading = Label(self.help_frame,
                                 text="Help/Instructions",
                                 font="arial 10 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (Label, Row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40,
                               bg=background, wrap=250)
        self.help_text.grid(collumn=0, row=1)
        
        # Dismiss button (Row 2)

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
