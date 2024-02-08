import tkinter as tk
import controller as c

# Function to be called when the button is clicked
def createNewNode():
    print("attempt")
    c.createNode
    print("attempted")
    output.set(c.output)

def search():
    c.search(toSearch, selectedSearch)
    output.set(c.output)
    

# Create the root window
root = tk.Tk()
root.title("Search Tree")


# Create a label widget
addNewNodeL = tk.Label(root, text="Add New Node")
addNewNodeL.pack()  # Pack the label into the root window

# Dropdown Menu Setup
parentOptions = c.nodes
selectedParent = tk.StringVar(root)
selectedParent.set(parentOptions[0])  # Set default value

# Create a label to display the selected option from the dropdown
selectedParentL = tk.Label(root, text="Select Parent")
selectedParentL.pack()  # Pack the label into the root window

# Create a dropdown menu for selecting a parent node
parentSelection = tk.OptionMenu(root, selectedParent, parentOptions)
parentSelection.pack()  # Pack the dropdown into the root window

# Create a label to prompt the text box
dataEntryL = tk.Label(root, text="Input data below")
dataEntryL.pack()  # Pack the label into the root window

#creates a textbox for data of new node
newNodeData = tk.StringVar(root)
dataEntry = tk.Entry(root, textvariable=newNodeData, background='white')
dataEntry.pack(padx=10, pady=10, fill='x', expand=True)

# Create a button that creates a new node
newNodeB = tk.Button(root, text="Create new node", command=createNewNode)
newNodeB.pack()  # Pack the button into the root window

#Sorting GUI

# Create a label to prompt search entry
searchEntryL = tk.Label(root, text="Input search below")
searchEntryL.pack()  # Pack the label into the root window

#creates a textbox for searched node
toSearch = tk.StringVar(root)
searchEntry = tk.Entry(root, textvariable=toSearch, background='white')
searchEntry.pack(padx=10, pady=10, fill='x', expand=True)

# Create a label to prompt search type
searchEntryL = tk.Label(root, text="select search type")
searchEntryL.pack()  # Pack the label into the root window

# Dropdown Menu Setup
searchOptions = ["BFS","DFS","IDS"]
selectedSearch = tk.StringVar(root)
selectedSearch.set(searchOptions[0])  # Set default value

# Create a button that creates a new node
searchB = tk.Button(root, text="Search", command=search)
searchB.pack()  # Pack the button into the root window

#Outputs

#label that gives output
output=tk.StringVar()
output.set("")
outputL = tk.Label(root, textvariable=output)
outputL.pack()

# Start the main event loop
root.mainloop()