import tkinter as tk
import logicsFinal
import constants as c

class Game2048(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title("2048")
        self.geometry(f'{c.SIZE}x{c.SIZE}')
        self.resizable(False, False)
        self.bind("<KeyPress>", self.key_down)
        self.commands = {c.KEY_UP: logicsFinal.move_up, c.KEY_DOWN: logicsFinal.move_down,
                         c.KEY_LEFT: logicsFinal.move_left, c.KEY_RIGHT: logicsFinal.move_right}
        
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()
    
    def init_grid(self):
        background = tk.Frame(self,
                              bg=c.BACKGROUND_COLOR_GAME)                            
        background.pack(expand=True, fill='both')

        #layout
        self.rowconfigure(list(range(c.GRID_LEN)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(c.GRID_LEN)), weight = 1, uniform = 'a')

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = tk.Frame(master=background, 
                                 bg=c.BACKGROUND_COLOR_CELL_EMPTY, 
                                 width=c.SIZE//c.GRID_LEN, 
                                 height=c.SIZE//c.GRID_LEN
                                 )
                cell.grid(row = i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)

                label = tk.Label(master=cell, text="", justify="center", background=c.BACKGROUND_COLOR_CELL_EMPTY,  font=c.FONT, width=2)
                label.pack(expand=True, fill='both')

                grid_row.append(label)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = logicsFinal.start_game()
        logicsFinal.add_new_2(self.matrix)
        logicsFinal.add_new_2(self.matrix)
    
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", background=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), background=c.BACKGROUND_COLOR_DICT[new_number], foreground=c.CELL_COLOR_DICT[new_number])

        self.update()

    def key_down(self, event):
        key = event.keysym
        print("key", key)
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)           
            if changed:
                logicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if logicsFinal.get_current_state(self.matrix)== 'WON':
                    self.grid_cells[1][1].configure(text="You", background=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", background= c.BACKGROUND_COLOR_CELL_EMPTY)
                
                if logicsFinal.get_current_state(self.matrix)== 'LOST':
                    self.grid_cells[1][1].configure(text="You", background=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", background= c.BACKGROUND_COLOR_CELL_EMPTY)

if __name__ == "__main__":
    Game2048()