import pygame
from scripts.Settings import *

class NPC:
    def __init__(self):
        pass


    def split_detect(self,board) -> bool:
        pass

    def edge_detect(self,board):
        pass

    def update(self,dt):
        pass

    def draw(self,screen):
        pass


class Red(NPC):
    def __init__(self):
        super().__init__()

    def split(self,board):

        if tile.value >= 4:
            self.reset_input()
            tile.value = 0
            if self.board[col-1][row].value < 0 or self.board[col+1][row].value < 0:
                self.board[col + 1][row].value = abs(self.board[col+1][row].value) + 1
                self.board[col - 1][row].value = abs(self.board[col-1][row].value) + 1
            else:
                self.board[col+1][row].value += 1
                self.board[col-1][row].value += 1

            if self.board[col][row+1].value < 0 or self.board[col][row-1].value < 0:
                self.board[col][row + 1].value = abs(self.board[col][row+1].value) + 1
                self.board[col][row - 1].value = abs(self.board[col][row-1].value) + 1
            else:
                self.board[col][row+1].value += 1
                self.board[col][row-1].value += 1