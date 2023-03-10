from tkinter import ttk

class ListComponent(ttk.Treeview):
    def __init__(self, *args, app, columns, rows, height=14, **kwargs):
        super().__init__(*args, selectmode="browse", show="headings", height=height, columns=columns, **kwargs)
        
        self.app = app

        self.yview_scroll(height, "units")

        for heading in columns:
            self.heading(heading, text=heading, anchor="w")
            self.column(column=heading, minwidth=10, width=20)

        for i in range(len(rows)):
            self.insert(parent="", index=i, values=rows[i])

        self.grid(row=0, column=0, columnspan=2, sticky="wes")

    def put_entries(self, new_items):
        old_items = self.get_children()
        for previous_item in old_items:
            self.delete(previous_item)
        
        for i in range(len(new_items)):
            self.insert(parent="", index=i, values=new_items[i])