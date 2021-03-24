from tkinter import *

from functools import partial  # To prevent unwanted windows (being created)

import random

import re


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

        # History / Help button frame (Row [1]) [From 02b_Converter_GUI_Version_2.py]
        self.history_help_buttons_frame = Frame(self.converter_frame)
        self.history_help_buttons_frame.grid(row=1)

        # History Button (Row 1, Column 0)
        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Arial", "12"),
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calculations_list))
        self.history_button.grid(row=1, column=0)

        if len(self.all_calculations_list) == 0:
            self.history_button.config(state=DISABLED)

        # Help Button (Row 1, Column 1) [From "01_Help_GUI.py"]
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "12"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1, column=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    def history(self, calculation_history):
        # print("You asked for the history segment of the program.") [This line is no longer necessary]
        History(self, calculation_history)


# Help Class (from "01_Help_GUI.py")
if __name__ == '__main__':
    class Help:

        # Set up initial function
        def __init__(self, partner):

            background = "orange"

            # Disable help button
            partner.help_button.config(state=DISABLED)

            # Sets up child window (or help box)
            self.help_box = Toplevel()

            # If users press cross at the top of the window, help closes and the help button 'releas[e]s'
            self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

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
            self.help_text.grid(row=1)

            # Dismiss button (Row 2)
            self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                         width =10, bg="pink", font="arial 10 bold",
                                         command=partial(self.close_help, partner))
            self.dismiss_button.grid(row=2, pady=10)

        # Defining close_help function
        def close_help(self, partner):

            # Put help button back into a normal state..
            partner.help_button.config(state=NORMAL)
            self.help_box.destroy()


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
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calculation_history))
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

    # Allows for "calculation_history" to continue to be referenced
    def export(self, calculation_history):
        Export(self, calculation_history)

# Export class from "12c_Export_GUI.py"


class Export:
    # Set up initial function
    def __init__(self, partner, calculation_history):

        print(calculation_history)

        background = "orange"

        # Disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (or export box)
        self.export_box = Toplevel()

        # If users press cross at the top of the window,
        # ... the export window closes and the export button 'releases'
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up export heading (Row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Calculation Export",
                                 font="arial 10 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # Export text (Label, Row 1)
        self.export_text = Label(self.export_frame, text="Enter a file name"
                                                         " in the box shown"
                                                         " below. Once this"
                                                         " is complete, press"
                                                         " the 'Save' button "
                                                         " to save your"
                                                         " calculation"
                                                         " history to a text"
                                                         " file.",
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=1)

        # File name entry box (Row 2)
        self.file_name_entry = Entry(self.export_frame, width=20,
                                     font="Arial 14 bold", justify=CENTER)
        self.file_name_entry.grid(row=2, pady=10)

        # Error message labels (Row 3) [This segment is initially blank]
        self.save_error_label = Label(self.export_frame, text="", fg="red",
                                      bg=background)
        self.save_error_label.grid(row=3)

        # Error message area (Row 4)
        self.export_text = Label(self.export_frame, text="If the file name"
                                                         " that you have "
                                                         " entered already"
                                                         " exists, the"
                                                         " file name's"
                                                         " contents will"
                                                         " be replaced with"
                                                         " your calculation"
                                                         " history",
                                 justify=LEFT, bg="yellow", fg="green",
                                 font="Arial 10 italic", wrap=200,
                                 padx=10, pady=10)
        self.export_text.grid(row=4, pady=10)

        # Save/Cancel Button(s) Frame (Row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (Row 0 of the "save_cancel_frame").
        # ... This portion of the code has been inspired by the file
        # ... titled "02c_Converter_GUI_Version_3.py".

        # Save Button
        self.save_button = Button(self.save_cancel_frame,
                                  text="Save", font="Arial 10 bold",
                                  command=partial(lambda: self.save_history(partner, calculation_history)),
                                  bg="pink", width=10)
        self.save_button.grid(row=0, column=0)

        self.dismiss_button = Button(self.save_cancel_frame,
                                     font="Arial 10 bold",
                                     text="Dismiss",
                                     command=partial(self.close_export, partner),
                                     bg="yellow", width=10)
        self.dismiss_button.grid(row=0, column=1)

    # Defining "save_history" function
    def save_history(self, partner, calculation_history):

        # Uses a regular expression to check of a file name is valid
        valid_character = "[A-Za-z0-9_]"
        has_error = "no"

        file_name = self.file_name_entry.get()
        print(file_name)

        for letter in file_name:
            if re.match(valid_character, letter):
                continue

            elif letter == " ":
                problem = "(Spaces are not allowed in this context)"

            else:
                problem = ("(The character of {} is not alowed in this context)".format(letter))

            has_error = "yes"
            break

        if file_name == "":
            problem = "The file name for this cannot be blank"
            has_error = "yes"

        if has_error == "yes":

            # Display Error Message
            self.save_error_label.config(text="Invalid file name - {}".format(problem))

            # Change entry box background to pink
            self.file_name_entry.config(bg="orange")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # Add .txt suffix to file name
            file_name = file_name + ".txt"

            # Create file to hold data
            f = open(file_name, "w+")

            # Add new line at end of each item
            for item in calculation_history:
                f.write(item + "\n")

            # Close file
            f.close()

            # Close dialogue
            self.close_export(partner)

    # Defining close_export function
    def close_export(self, partner):
        # Put export button back into a normal state..
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
