from tkinter import Button, Label, DISABLED, NORMAL
import random
from data import MINES_COUNT, CELL_COUNT
import ctypes
import sys


class Cell :
    all = []
    cell_count_label_object = None
    cell_count = CELL_COUNT

    def __init__(self, x, y, is_mine = False) :
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y


        Cell.all.append(self)

    
    def __repr__(self) :
        return f'Cell({self.x}, {self.y})'


    def create_btn_object(self, location) :
        btn = Button(location, width = 12, height = 4)

        btn.bind('<Button-1>', self.left_click_actions) # left click
        btn.bind('<Button-3>', self.right_click_actions) # right click


        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location) :
        lbl = Label(location, text = f'Cells left : {Cell.cell_count}', width= 12, height=4, bg = 'black', fg = 'white', font = ('', 30))
        
        Cell.cell_count_label_object = lbl

    
    def left_click_actions(self, event) :
        if self.is_mine :
            self.show_mine()
        else :
            if self.surrouned_cells_mines_leght == 0 :
                for cell_obj in self.surrouned_cells :
                    cell_obj.show_cell()

            self.show_cell()
            # if mines count is equal to cellss left count player won
            if Cell.cell_count == MINES_COUNT :
                ctypes.windll.user32.MessageBoxW(0, 'Congratualtions !!!', 'You Won', 0)
                sys.exit()



        # cancel events of button if cell is opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')






    def get_cell_by_axis(self, x, y) :
        for cell in Cell.all :
            if cell.x == x and cell.y == y :
                return cell


    @property
    def surrouned_cells(self) :
        cells = [cell for cell in

            [self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)]

            if cell is not None
        ]

        return cells


    @property
    def surrouned_cells_mines_leght(self) :
        counter = 0

        for cell in self.surrouned_cells :
            if cell.is_mine :
                counter += 1

        return counter





    def show_mine(self) :
        self.cell_btn_object.configure(bg = 'red')

        ctypes.windll.user32.MessageBoxW(0, 'You clicked on mine', 'Game Over', 0)
        sys.exit()

    def show_cell(self) :
        if not self.is_open :
            Cell.cell_count -= 1

            self.cell_btn_object.configure(text = self.surrouned_cells_mines_leght)
            # rewrite the text pf cell count label with newer count
            if Cell.cell_count_label_object :
                Cell.cell_count_label_object.configure(
                    text = f'Cells left : {Cell.cell_count}'
                )

            #mark cell as open
            self.is_open = True
            # if was mine candidaet change bg back to original color
            self.cell_btn_object.configure(bg = 'SystemButtonFace')





    def right_click_actions(self, event) :
        if not self.is_mine_candidate :
            self.is_mine_candidate = True
            self.cell_btn_object.configure(bg = 'orange')
            
        else :
            self.is_mine_candidate = False
            self.cell_btn_object.configure(bg = 'SystemButtonFace')



    
    @staticmethod
    def randomize_mines() : 
        picked_cells = random.sample(Cell.all, MINES_COUNT)

        for picked_cell in picked_cells :
            picked_cell.is_mine = True     



