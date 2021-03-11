from tkinter import *

from functools import partial  # To prevent unwanted windows (being created)

import random


class Converter:

    def __init__(self, parent):

        # Formatting variables...
        background_color = "purple"

        # In the actual program. this will be blank, and populated with user calculation(s)
        self.all_calculations_list = ['1 degrees fahrenheit is -17.2 degrees celsius',
                                      '2 degrees celsius is 35.6 degrees fahrenheit',
                                      '3 degrees fahrenheit is -16.1 degrees celsius']

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

        # history Button (Row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Arial", "12"),
                                     padx=10, pady=10,
                                     command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        print("You asked for history")
        get_history = History(self)
        get_history.history_text.configure(text="History text goes here")


if __name__ == '__main__':
    class History:

        # Set up initial function
        def __init__(self, partner):

            background = "green"

            # Disable history button
            partner.history_button.config(state=DISABLED)

            # Sets up child window (or history box)
            self.history_box = Toplevel()

            # If users press cross at the top of the window, history closes and the history button 'releases'
            self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

            # Set up GUI Frame
            self.history_frame = Frame(self.history_box, bg=background)
            self.history_frame.grid()

            # Set up history heading (Row 0)
            self.how_heading = Label(self.history_frame,
                                     text="History/Instructions",
                                     font="arial 10 bold",
                                     bg=background)
            self.how_heading.grid(row=0)

            # history text (Label, Row 1)
            self.history_text = Label(self.history_frame,
                                      text="Here are the most recently completed calculations."
                                           "Please use the export button to create a text file"
                                           " of all your calculations for this session.",
                                      font="arial 10 italic",
                                      justify=LEFT, width=40, fg="light orange",
                                      bg=background, wrap=250)
            self.history_text.grid(row=1)

            # Show user their [calculation] history (Row 2)

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
