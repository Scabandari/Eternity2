

class Piece:

    def __init__(self, name, left, right, bottom):
        self.name = name
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = None
        self.inverted = False
        self.rotations = 0  # rotations are always right
        self.corner_piece = False
        self.side_piece = False

    def rotate(self):
        if self.inverted:
            assert(self.bottom is None and self.top is not None),\
                "Piece is inverted and either has no top or has a bottom"
            self.bottom = self.right
            self.right = self.top
            self.top = None
            self.inverted = False
            self.rotations = 0 if ((self.rotations + 1) % 6 == 0) else self.rotations + 1

        else:
            assert(self.bottom is not None and self.top is None), \
                "Uninverted piece but either has a top or has no bottom"
            self.top = self.left
            self.left = self.bottom
            self.bottom = None
            self.inverted = True
            self.rotations = 0 if ((self.rotations + 1) % 6 == 0) else self.rotations + 1


    def __str__(self):
        return "{}, L:{}, R:{}, T:{}, B:{}, Rot:{}"\
            .format(self.name, self.left, self.right, self.top, self.bottom, self.rotations)

    def print_verbose(self):
        print("{}: left: {}, right: {}, top: {}, bottom: {}, rotations: {}" \
            .format(self.name, self.left, self.right, self.top, self.bottom, self.rotations))

    def count_zeros(self):
        """This helps determine if pieces are corner or side pieces. """
        zeros = 0
        if self.right == 0:
            zeros += 1
        if self.left == 0:
            zeros += 1
        if self.bottom == 0:
            zeros += 1
        if self.top == 0:
            zeros += 1
        return zeros





