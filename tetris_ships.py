"""'Tetris' ship types for the Battleship game.

   Author: Russ Lewis

   Defines a series of functions, producing ships which are shaped like
   the classic pieces from Tetris.  In all cases, (0,0) is included as
   one of the points in the set.

   As with the standard ship functions, these all accept a 'rot'
   parameter, which is used to rotate the ship as it is being created.

   Primary functions:
      Tee     (rot)
      R_ZigZag(rot)
      L_ZigZag(rot)
      L_Boot  (rot)
      R_Boot  (rot)
      Square  (rot)
      Bar     (rot)

   Imports a utility function:
      rotate_shape(), imported from standard_ships.py
"""



from battleship     import Ship,Pos
from standard_ships import rotate_shape



def Tee(rot):
    """Tetris Ship 'Tee'
       .
       .        T
       Shape: T T T
    """

    return Ship("Tee",
                rotate_shape([Pos(0,0), Pos(1,0), Pos(0,1), Pos(-1,0)], rot))

def R_ZigZag(rot):
    """Tetris Ship 'Right ZigZag'
       .
       .        R
       .      R R
       Shape: R
    """

    return Ship("R Zig-Zag",
                rotate_shape([Pos(0,0), Pos(0,1), Pos(1,1), Pos(1,2)], rot))

def L_ZigZag(rot):
    """Tetris Ship 'Left ZigZag'
       .
       .      L
       .      L L
       Shape:   L
    """

    return Ship("L Zig-Zag",
                rotate_shape([Pos(0,0), Pos(0,1), Pos(-1,1), Pos(-1,2)], rot))

def L_Boot(rot):
    """Tetris Ship 'Left Boot'
       .
       .      L
       .      L
       Shape: L L
    """

    return Ship("L Boot",
                rotate_shape([Pos(0,0), Pos(1,0), Pos(0,1), Pos(0,2)], rot))

def R_Boot(rot):
    """Tetris Ship 'Right Boot'
       .
       .        R
       .        R
       Shape: R R
    """

    return Ship("R Boot",
                rotate_shape([Pos(0,0), Pos(-1,0), Pos(0,1), Pos(0,2)], rot))

def Square(rot):
    """Tetris Ship 'Square'
       .
       .      S S
       Shape: S S
    """

    return Ship("Square",
                rotate_shape([Pos(0,0), Pos(1,0), Pos(0,1), Pos(1,1)], rot))

def Bar(rot):
    """Tetris Ship 'Bar'
       .
       Shape: B B B B
    """

    return Ship("Bar",
                rotate_shape([Pos(0,0), Pos(1,0), Pos(2,0), Pos(3,0)], rot))


