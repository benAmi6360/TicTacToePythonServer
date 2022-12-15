"""Imports the MarkType enum (defines a square as Free or Taken)"""
from mark_type import MarkType

class GameBoard:
    """Class for managing the game board"""
    def __init__(self):
        self._board = self.initialize_grid()


    def is_board_full(self):
        """Checks if the game board is full"""
        for row in self._board:
            for square in row:
                if square == MarkType.FREE:
                    return False
        return True


    def initialize_grid(self):
        """Initiates the game board (grid)"""
        grid = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(MarkType.FREE)
            grid.append(row)
        return grid


    def get_cords(self, cords_dict):
        """Gets cordinates of square from a dict"""
        cords = []
        for key in cords_dict.keys():
            cords.append(int(cords_dict[key]))
        return cords


    def update_board(self, cords_dict: dict, who_took: bool) -> None:
        """Update the game board according to the changes"""
        mark_type = MarkType.CIRCLE if who_took else MarkType.CROSS
        cords = self.get_cords(cords_dict)
        self._board[cords[0]][cords[1]] = mark_type


    def validate_square(self, cords_dict: dict) -> bool:
        """Checks if square is taken or free"""
        cords = self.get_cords(cords_dict)
        return self._board[cords[0]][cords[1]] == MarkType.FREE
