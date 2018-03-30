#!/usr/bin/env/ python3
import csv
from piece import Piece
from arrangement import Arrangement

CSV_FILE = 'input.csv'

reg_pieces = []
corner_pieces = []
side_pieces = []

with open(CSV_FILE) as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    iter_csv = iter(readCSV)
    for row in iter_csv:
        if len(row) < 1:
            break
        name = row.pop(0)
        left = int(row.pop(0))
        right = int(row.pop(0))
        bottom = int(row.pop(0))
        piece = Piece(name, left, right, bottom)
        zeros = piece.count_zeros()
        if zeros == 2:
            corner_pieces.append(piece)
        elif zeros == 1:
            side_pieces.append(piece)
        else:
            reg_pieces.append(piece)

print("Get to work asshole")

# print("Corner Pieces: ")
# for p in corner_pieces:
#     p.print_verbose()
#
# print("Side Pieces: ")
# for p in side_pieces:
#     p.print_verbose()
#
# print("Regular Pieces: ")
# for p in reg_pieces:
#     p.print_verbose()

arr = Arrangement(corner_pieces, side_pieces, reg_pieces)
arr.create()

arr.show_()

print(arr.get_fitness())

"""This is just to test to make sure my fitness functions is working"""
c = Piece("C", 0, 0, 6)
c.rotate()
top = [c]
I = Piece("I", 3, 0, 2)
for i in range(4):
    I.rotate()
mid = [I]

a = Piece("A", 4, 2, 6)
for i in range(3):
    a.rotate()
mid.append(a)

f = Piece("F", 0, 5, 4)
f.rotate()
f.rotate()
mid.append(f)

g = Piece("G", 0, 0, 2)
for i in range(4):
    g.rotate()
bottom = [g]

h = Piece("H", 1, 2, 3)
for i in range(3):
    h.rotate()
bottom.append(h)

d = Piece("D", 1, 4, 0)
bottom.append(d)

e = Piece("E", 3, 4, 5)
for i in range(3):
    e.rotate()
bottom.append(e)

b = Piece("B", 0, 3, 0)
for i in range(4):
    b.rotate()
bottom.append(b)

zero_fitness = Arrangement(top, mid, bottom)
print("fitness zero:", zero_fitness.get_fitness())
print("fitness random:", arr.get_fitness())







