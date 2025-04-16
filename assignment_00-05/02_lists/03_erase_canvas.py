import tkinter as tk

class EraserCanvas:
    def __init__(self, root, width=600, height=400, cell_size=20):
        self.root = root
        self.canvas = tk.Canvas(root, width=width, height=height, bg='white')
        self.canvas.pack()
        
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.cells = {}
        
        # Draw grid
        self.draw_grid()
        
        # Create eraser (a rectangle that will erase cells)
        self.eraser = self.canvas.create_rectangle(0, 0, cell_size, cell_size, outline='black', fill='gray', width=2)
        
        # Bind mouse events for dragging the eraser
        self.canvas.bind('<B1-Motion>', self.move_eraser)
        self.canvas.bind('<ButtonRelease-1>', self.erase_cells)
        
    def draw_grid(self):
        """Draw the initial grid of blue cells."""
        for y in range(0, self.height, self.cell_size):
            for x in range(0, self.width, self.cell_size):
                rect = self.canvas.create_rectangle(x, y, x+self.cell_size, y+self.cell_size, fill='blue', outline='black')
                self.cells[rect] = (x, y)
    
    def move_eraser(self, event):
        """Move the eraser rectangle with the mouse."""
        x1, y1, x2, y2 = self.canvas.coords(self.eraser)
        x = event.x - self.cell_size // 2
        y = event.y - self.cell_size // 2
        self.canvas.coords(self.eraser, x, y, x + self.cell_size, y + self.cell_size)
        
    def erase_cells(self, event):
        """Erase the cells that the eraser rectangle is in contact with."""
        eraser_coords = self.canvas.coords(self.eraser)
        eraser_x1, eraser_y1, eraser_x2, eraser_y2 = eraser_coords
        
        for rect, (x, y) in self.cells.items():
            # Check if the eraser rectangle intersects with any cell
            if (eraser_x1 < x + self.cell_size and eraser_x2 > x and 
                eraser_y1 < y + self.cell_size and eraser_y2 > y):
                self.canvas.itemconfig(rect, fill='white')

# Create the main Tkinter window
root = tk.Tk()
root.title("Canvas Eraser Tool")

# Create the EraserCanvas
eraser_canvas = EraserCanvas(root)

# Start the Tkinter event loop
root.mainloop()
