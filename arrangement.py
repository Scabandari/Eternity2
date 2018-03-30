from random import shuffle
from copy import deepcopy


class Arrangement:

    def __init__(self, corners, side_pieces, pieces):
        self.corners = deepcopy(corners)  # every arrangement needs its own copy of the pieces
        self.side_pieces = deepcopy(side_pieces)
        self.pieces = deepcopy(pieces)
        self.board = []
        for list_ in (self.corners, self.side_pieces, self.pieces):
            shuffle(list_)

    def add_top(self):
        piece = self.corners.pop()
        counter = 0
        while (piece.left != 0) or (piece.right != 0):
            assert (counter < 8), "add_top() is running endlessly"
            piece.rotate()
            counter += 1
        row1 = [piece]
        self.board.append(row1)

    def add_row(self, iteration):  # todo add assert statement to make sure no infinite loop
        num_pieces = (iteration - 1) * 2 + 1
        row = []
        left_side = self.side_pieces.pop(0)  # add left side piece
        counter = 0
        while left_side.left != 0 or left_side.top is not None:
            assert(counter < 8), "add_row is running endlessly"
            left_side.rotate()
        row.append(left_side)

        for index in range(num_pieces):  # add the middle pieces, rotate as necessary
            piece_ = self.pieces.pop(0)
            counter = 0
            if index % 2 == 0:
                while piece_.top is None:
                    assert (counter < 3), "add_row is running endlessly"
                    piece_.rotate()
                    counter += 1
            else:
                while piece_.top is not None and piece_.bottom is None:
                    assert (counter < 3), "add_row is running endlessly"
                    piece_.rotate()
                    counter += 1
            row.append(piece_)

        right_side = self.side_pieces.pop(0)  # add right side piece
        counter = 0
        while right_side.right != 0 or right_side.top is not None:
            assert (counter < 8), "add_row is running endlessly"
            right_side.rotate()
        row.append(right_side)
        self.board.append(row)

    def add_bottom(self, row_number):
        row = []
        left_corner = self.corners.pop(0)
        counter = 0
        while left_corner.left != 0 or left_corner.bottom != 0:  # add bottom left corner
            assert(counter < 8), "add_bottom running endlessly, left corner"
            left_corner.rotate()
            counter += 1
        row.append(left_corner)

        for index in range(row_number):   # add remaining side pieces to the inner bottom
            if index % 2 == 0:
                piece = self.pieces.pop(0)
                counter = 0
                while piece.top is None:
                    assert (counter < 3), "add_bottom running endlessly"
                    piece.rotate()
                    counter += 1
                row.append(piece)
            else:
                bottom_piece = self.side_pieces.pop()
                counter = 0
                while bottom_piece.bottom != 0:
                    assert(counter < 8), "add_bottom running endlessly, inner bottom"
                    bottom_piece.rotate()
                    counter += 1
                row.append(bottom_piece)

        right_corner = self.corners.pop(0)
        counter = 0
        while right_corner.bottom != 0 or right_corner.right != 0:
            assert(counter < 4), "add_bottom running endlessly, right corner"
            right_corner.rotate()
            counter += 1
        row.append(right_corner)

        self.board.append(row)

    def create(self):
        self.add_top()
        remaining_pieces = len(self.corners) + len(self.side_pieces) + len(self.pieces)
        iter_ = 1
        while remaining_pieces > (iter_ + 1) * 2 + 1:
            self.add_row(iter_)
            iter_ += 1
            remaining_pieces = len(self.corners) + len(self.side_pieces) + len(self.pieces)
        self.add_bottom((iter_ - 1) * 2 + 1)

    def show_(self):
        """Prints the Arrangement for visual inspections by humans"""
        row_num = 0
        for index, list_ in enumerate(self.board):
            print("Row {}".format(index))
            for piece in list_:
                print(piece,)
            else:
                print()

    def get_fitness(self):
        penalty = 0
        num_rows = len(self.board)
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                # check if its the top piece
                if i == 0:
                    if piece.bottom != self.board[i+1][j+1].top:
                        penalty += 1
                    continue

                # check if it's the bottom row
                if i == len(self.board) - 1:
                    # bottom corners
                    if j == 0:
                        if piece.right != self.board[i][j+1].left:
                            penalty += 1
                        continue

                    elif j == len(row) - 1:
                        if piece.left != self.board[i][j-1].right:
                            penalty += 1
                        continue

                    # the rest of the bottom
                    else:
                        if piece.top is not None:
                            if piece.top != self.board[i-1][j-1].bottom:
                                penalty += 1
                        if piece.left != self.board[i][j-1].right:
                            penalty += 1
                        if piece.right != self.board[i][j+1].left:
                            penalty += 1
                        continue

                # from here on we know we're dealing with a piece that's not in the top or bottom rows
                # check the two end pieces for the row
                if j == 0:
                    if piece.right != self.board[i][j+1].left:
                        penalty += 1
                    if piece.bottom != self.board[i+1][j+1].top:
                        penalty += 1
                    continue

                if j == len(row) - 1:
                    if piece.left != self.board[i][j - 1].right:
                        penalty += 1
                    if piece.bottom != self.board[i+1][j+1].top:
                        penalty += 1
                    continue

                # finally we're dealing with pieces not in the first row, last row or side pieces
                if piece.top is not None:
                    if piece.top != self.board[i-1][j-1].bottom:
                        penalty += 1
                else:
                    if piece.bottom != self.board[i+1][j+1].top:
                        penalty += 1
                if piece.left != self.board[i][j+1].right:
                    penalty += 1
                if piece.right != self.board[i][j-1].left:
                    penalty += 1
        return penalty













