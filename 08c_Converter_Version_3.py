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
        self.converter_frame = Frame(bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature converter heading (Row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font=("Arial", "20", "bold"),
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
                                             wrap=290, justify=LEFT,
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
                                  text="To Celsius", font="Arial 10 bold",
                                  bg="lime", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="orange", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (Row 4)
        self.converted_label = Label(self.converter_frame,
                                     text="Conversion goes here...",
                                     font=("Arial", "10", "italic"),
                                     wrap=250, padx=10, pady=10,
                                     fg="white", bg=background_color,)
        self.converted_label.grid(row=4)

        # History / Help button frame (Row 5)
        self.history_help_buttons_frame = Frame(self.converter_frame)
        self.history_help_buttons_frame.grid(row=5, pady=10)

        self.history_button = Button(self.history_help_buttons_frame,
                                          text="History", font="Arial 10 bold",
                                          bg="pink", width=10)
        self.history_button.grid(row=0, column=0)

        if len(self.all_calculations_list) == 0:
            self.history_button.config(state=DISABLED)

    # Defining Converter
    def temp_convert(self, low):

        print(low)

        error = "white"  # Shows this colour when an entry has errors

        # Retrieve amount entered into "Entry" field
        to_convert = self.to_convert_entry.get()

        # Check amount is a valid number
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to degrees Fahrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees celsius is {} degrees fahrenheit".format(to_convert, fahrenheit)

            # Check and convert to degrees Celsius
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees fahrenheit is {} degrees celsius".format(to_convert, celsius)

            # If the entry is not a valid temperature
            else:
                answer = "This temperature entry is too cold, and therefore not valid."
                has_errors = "yes"

            # Display converted value

            # If no error is present
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="lime")
                self.to_convert_entry.configure(bg="white")

            # If an error is present
            else:
                self.converted_label.configure(text=answer,
                                               fg="pink")
                self.to_convert_entry.configure(bg=error)

            # Add answer to list for "History" purposes
            if answer != "This temperature entry is too cold, and therefore not valid.":
                self.all_calculations_list.append(answer)
                print(self.all_calculations_list)

        # Print an error message is applicable
        except ValueError:
            self.converted_label.configure(text="Please enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)

    # Value rounding function

    def round_it(self, to_round):

        if to_round % 1 == 0:
            rounded = int(to_round)

        else:
            rounded = round(to_round, 1)

        return rounded

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
