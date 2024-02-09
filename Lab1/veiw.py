import tkinter as tk
import controller as c

# Function to be called when the button is clicked
def createNewNode():
    outputL.config(text=c.createNode(newNodeData.get(), selectedParent.get()))
    #code from chat GPT bellow
    menu = parentSelection['menu']
    menu.delete(0, 'end')

    # Add new options from c.nodes
    for node in c.nodes:
        menu.add_command(label=node, command=lambda value=node: selectedParent.set(value))
   
def search():
    outputL.config(text=c.search(toSearch.get(), selectedSearch.get()))
    
    

# Create the root window
root = tk.Tk()
root.title("Search Tree")


# Create a label widget
addNewNodeL = tk.Label(root, text="Add New Node")
addNewNodeL.pack()  # Pack the label into the root window

# Dropdown Menu Setup
selectedParent = tk.StringVar(root)
selectedParent.set(c.nodes[0])  # Set default value

# Create a label to display the selected option from the dropdown
selectedParentL = tk.Label(root, text="Select Parent")
selectedParentL.pack()  # Pack the label into the root window

# Create a dropdown menu for selecting a parent node
parentSelection = tk.OptionMenu(root, selectedParent, c.nodes)
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

# search type Dropdown Menu Setup
searchOptions = ["BFS", "DFS","IDS"]
selectedSearch = tk.StringVar(root)
selectedSearch.set(searchOptions[0])  # Set default value

# Create a dropdown menu for selecting a search type
searchSelection = tk.OptionMenu(root, selectedSearch, *searchOptions)
searchSelection.pack()  # Pack the dropdown into the root window

# Create a button that creates a new node
searchB = tk.Button(root, text="Search", command=search)
searchB.pack()  # Pack the button into the root window

#Outputs

#label that gives output
outputL = tk.Label(root, text="test")
outputL.pack()

# Start the main event loop
root.mainloop()