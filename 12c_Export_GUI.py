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

        # Export Button (Row 1)
        self.export_button = Button(self.converter_frame, text="Export",
                                    font=("Arial", "12"),
                                    padx=10, pady=10,
                                    command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        print("You asked for an export window")
        get_export = Export(self)


if __name__ == '__main__':
    class Export:

        # Set up initial function
        def __init__(self, partner):

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

            # Error message area (Row 3)
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
            self.export_text.grid(row=3, pady=10)

            # Save/Cancel Button(s) Frame (Row 4)
            self.save_cancel_frame = Frame(self.export_frame)
            self.save_cancel_frame.grid(row=4, pady=10)

            # Save and Cancel Buttons (Row 0 of the "save_cancel_frame").
            # ... This portion of the code has been inspired by the file
            # ... titled "02c_Converter_GUI_Version_3.py".

            # Save Button
            self.save_button = Button(self.save_cancel_frame,
                                      text="Save", font="Arial 10 bold",
                                      bg="pink", width=10)
            self.save_button.grid(row=0, column=0)

            self.dismiss_button = Button(self.save_cancel_frame,
                                        font="Arial 10 bold",
                                        text="Dismiss",
                                        command=partial(self.close_export, partner),
                                        bg="yellow", width=10)
            self.dismiss_button.grid(row=0, column=1)

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
