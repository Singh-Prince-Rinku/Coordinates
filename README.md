# This Python script creates a simple GUI application using tkinter to display the coordinates of mouse clicks relative to the application window

When you run the script, a tkinter window titled "Click Coordinates" opens.
The window displays a label instructing the user to click inside the window.
When the user clicks inside the window, the on_click method calculates the relative coordinates of the click with respect to the top-left corner of the window.
These coordinates are then displayed in the self.coord_label label.
Closing the tkinter window stops the mouse listener (self.listener.stop()).
