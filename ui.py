import tkinter as tk
from tkinter import ttk
import pandas as pd

class DataFrameViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("DataFrame Viewer")

        # Create a DataFrame (You can replace this with your own data)
        data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                'Age': [25, 30, 35, 40]}
        self.df = pd.DataFrame(data)

        # Create a Treeview widget to display the DataFrame
        self.tree = ttk.Treeview(self.root, columns=list(self.df.columns), show="headings")

        # Set column headings
        for column in self.df.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=100)

        # Insert data into the Treeview
        for index, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the Treeview widget
        self.tree.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataFrameViewer(root)
    root.mainloop()
