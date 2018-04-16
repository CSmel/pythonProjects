# Name and Adress GUI
import tkinter
import tkinter.messagebox

class FahConverterGUI:
    # Create the main window.
    def __init__(self):
        self.main_window = tkinter.Tk()
  
        
        
        
        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        

        # Create widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, \
                    text='Enter the Celsius temperature:')
        self.fah_entry = tkinter.Entry(self.top_frame,  \
                                       width=10)
        self.degree_1_label = tkinter.Label(self.top_frame, \
                    text='°C')
        
        
        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.fah_entry.pack(side='left')
        self.degree_1_label.pack(side='left')

        # Create widgets for the middle frame.
        self.descr_label = tkinter.Label(self.mid_frame,  \
                                         text='Converted to Fahrenheit: ')

        # We need a StringVar object to associate with
        # and output label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()
        self.fah_label = tkinter.Label(self.mid_frame, \
                                       textvariable=self.value)
        self.degree_label = tkinter.Label(self.mid_frame,  \
                                         text='°F')

        # Pack the middle frame's widgets.
        self.descr_label.pack(side='left')
        self.fah_label.pack(side='left')
        self.degree_label.pack(side='left')
       
                            

        # Create button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, \
                                        text='Convert', \
                                        command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the calculate button.

    def convert(self):
        c = float(self.fah_entry.get())

        # Convert.
        f =  (9/5) * c + 32

        # Convert C to a string and store it in the StringVar object.  This will
        # automatically update the fah_label widget.
        self.value.set(f)
        
        
       # Create an instance of the MyGUI class.
celsius_fah_convert = FahConverterGUI()
