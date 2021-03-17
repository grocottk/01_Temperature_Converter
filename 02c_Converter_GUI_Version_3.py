
# This version of the code is not very useful in practice

from tkinter import *

from functools import partial  # To prevent unwanted windows (being created)

import random


class Converter:

    def __init__(self, parent):
        # Formatting variables
        background_color = "medium purple"

        # Initialise list to hold calculation history
        self.all_calculations_list = []

        # Converter frame
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature converter heading (Row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font=("Arial", "18", "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User Instructions (Row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to"
                                                  " be converted and then"
                                                  " push one of the buttons"
                                                  " below...",
                                             font=("Arial", "10", "italic"),
                                             wrap=250, justify=LEFT,
                                             bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (Row 2)
        self.to_convert_entry = Entry(self.converter_frame,
                                      width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (Row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="lime", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="orange", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer label (Row 4)
        self.answer_label = Label(self.converter_frame,
                                  text="Answer goes here...",
                                  font=("Arial", "10", "italic"),
                                  wrap=250, padx=10, pady=10,
                                  fg="midnight blue", bg=background_color,)
        self.answer_label.grid(row=4)

        # History / Help button frame (Row 5)
        self.history_help_buttons_frame = Frame(self.converter_frame)
        self.history_help_buttons_frame.grid(row=5, pady=10)

        self.history_button = Button(self.history_help_buttons_frame,
                                     text="History", font="Arial 10 bold",
                                     bg="pink", width=10,
                                     command=lambda: self.history(self.all_calculations_list))
        self.history_button.grid(row=0, column=0)

        # Disables button if nothing is present in the list.
        if len(self.all_calculations_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.history_help_buttons_frame,
                                  text="Help", font="Arial 10 bold",
                                  bg="yellow", width=10)
        self.help_button.grid(row=0, column=1)

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
