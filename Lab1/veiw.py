import tkinter as tk
import controller

# Function to be called when the dropdown option changes
def on_option_change(selection):
    selected_option_label.config(text=f"Selected: {selection}")

# Function to be called when the button is clicked
def on_click():
    print(f"Button clicked! Current selection: {selected_option.get()}")

# Create the root window
root = tk.Tk()
root.title("Search Tree")

# Dropdown Menu Setup
options = controller.nodes
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set default value

# Create a label widget
addNewNodeL = tk.Label(root, text="Add New Node")
addNewNodeL.pack()  # Pack the label into the root window

# Create a label to display the selected option from the dropdown
selected_option_label = tk.Label(root, text=f"Selected: {selected_option.get()}")
selected_option_label.pack()  # Pack the label into the root window

# Create a dropdown menu for selecting a parent node
parentSelection = tk.OptionMenu(root, selected_option, *options, command=on_option_change)
parentSelection.pack()  # Pack the dropdown into the root window

# Create a button widget
button = tk.Button(root, text="Click me!", command=on_click)
button.pack()  # Pack the button into the root window

# Start the main event loop
root.mainloop()