from tkinter import *
from data import *
from support_func import *
from cell import Cell


root = Tk()

root.title('Minesweeper')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.config(bg = 'black')
root.resizable(False, False)




titel_frame = Frame(root, bg='black', width = WIDTH, height = get_percent(HEIGHT, 15))
titel_frame.place(x = 0, y = 0)


side_frame = Frame(root, bg='black', width = get_percent(WIDTH, 20), height = get_percent(HEIGHT, 85))
side_frame.place(x = 0, y = get_percent(HEIGHT, 15))


main_frame = Frame(root, bg='black', width = get_percent(WIDTH, 80), height = get_percent(HEIGHT, 85))
main_frame.place(x = get_percent(WIDTH, 20), y = get_percent(HEIGHT, 15))


game_title = Label(titel_frame, bg = 'black', fg = 'white', text = 'MINESWEEPER', font = ('', 48))
game_title.place(x = get_percent(WIDTH, 25), y = 0)


for x in range(GRID_SIZE) :
    for y in range(GRID_SIZE) :
        c1 = Cell(x, y)
        c1.create_btn_object(main_frame)
        c1.cell_btn_object.grid(column=x, row=y)

# call the label from cell class

Cell.create_cell_count_label(side_frame)
Cell.cell_count_label_object.place(x = 0, y =0)

Cell.randomize_mines()




root.mainloop()