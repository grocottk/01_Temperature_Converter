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

        # History Button (Row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Arial", "12"),
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calculations_list))
        self.history_button.grid(row=1)

        if len(self.all_calculations_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calculation_history):
        # print("You asked for the history segment of the program.") [This line is no longer necessary]
        History(self, calculation_history)


class History:

    # Set up initial function
    def __init__(self, partner, calculation_history):

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
                                 text="Calculation History",
                                 font="arial 19 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # History text (Label, Row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are the most recently completed calculations."
                                       " Please use the export button to create a text file"
                                       " of all your calculations for this session (if desired).",
                                  font="arial 10 italic",
                                  justify=LEFT, width=40, fg="orange",
                                  bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Dismiss button (Row 2)
        self.dismiss_button = Button(self.history_frame, text="Dismiss",
                                     width=10, bg="orange", font="arial 10 bold",
                                     command=partial(self.close_history, partner))

        # History output: (Row 2)

        # Generate string from list of calculations:
        history_string = ""

        # Defining "empty string"
        if len(calculation_history) >= 7:
            for item in range(0, 7):
                history_string += calculation_history[len(calculation_history)
                                                      - item - 1]+"\n"

        # This code may come into effect when a small number of "calculation_history"
        # ... entries have been created.
        else:
            for item in calculation_history:
                history_string += calculation_history[len(calculation_history) -
                                                      calculation_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here are your complete calculations."
                                              " Please use the export button to create a text file"
                                              " of the calculations for this session (if desired).")

        # Label to display calculation history to user
        self.calculation_label = Label(self.history_frame, text=history_string,
                                       bg=background, font="Arial 12", justify=LEFT)
        self.calculation_label.grid(row=2)

        # Export / Dismiss buttons frame (Row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     # (use of 'partner' parameter from 01_Help_GUI.py)
                                     font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    # Closes history
    def close_history(self, partner):

        # Put history button back to normal:
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    # Show user their [calculation] history (Row 2)

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
