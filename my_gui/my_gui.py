# Name and Adress GUI
import tkinter

class MyGUI:
    # Create the main window.
    def __init__(self):
        self.main_window = tkinter.Tk()
       
        # Create StringVar objects to display name,
        # street, and city-state-zip.
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()
        
        # Create two frame.
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create the label widgets, associated with the
        # StringVar objects.
        self.name_label = tkinter.Label(self.info_frame,\
                                        textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame,\
                                          textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame,\
                                       textvariable=self.csz_value)
                                            

        # Pack the labels.
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # Create the button widgets.
        self.show_info_button = tkinter.Button(self.button_frame, \
                                               text='Show Info', \
                                               command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        # Pack the buttons.
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Pack the frames.
        self.info_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()


        # Callback function for the Show Info button.

    def show(self):
        self.name_value.set('Matt Hoyle')
        self.street_value.set('123 Walnut Street')
        self.csz_value.set('Asheville, NC  29999')
    
# Create an instance of the MyGUI class.
my_gui = MyGUI()
