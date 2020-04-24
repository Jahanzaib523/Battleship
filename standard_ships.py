"""Standard ship types for the Battleship game.

   Author: Russ Lewis

   Defines a function for each of the well-known ship types in Battleship;
   the function creates a new Ship object every time that it is called.
   The code in this module builds a standard shape, which always includes
   the point (0,0); the caller passes these functions a 'rot' field, which
   is used to rotate the shape before we pass it to the Ship constructor.

   Primary functions:
      Carrier   (rot)
      Battleship(rot)
      Cruiser   (rot)
      Submarine (rot)
      Destroyer (rot)

   Utility functions:
      rotate_shape(shape,rot)
"""


from battleship import Ship, Pos


def rotate_shape(shape, rot):
    """Given a shape and a rotation amount (0 through 3, inclusive) return the
       shape after every point has been rotated around the origin.  Note that
       the 'rot' field here has the same semantics as the 'rot' field of the
       Pos.rotate() method: namely, that the value represents how many 90-degree
       clockwise turns to perform.
    """

    if rot == 0:
        return shape

    retval = []
    for pos in shape:
        temp = pos.rotate(rot)
        retval.append(temp)
    return retval


def Carrier(rot):
    return Ship("Aircraft Carrier",
                rotate_shape([Pos(0, 0), Pos(1, 0), Pos(2, 0), Pos(3, 0), Pos(4, 0)], rot))


def Battleship(rot):
    return Ship("Battleship",
                rotate_shape([Pos(0, 0), Pos(1, 0), Pos(2, 0), Pos(3, 0)], rot))


def Cruiser(rot):
    return Ship("Cruiser",
                rotate_shape([Pos(0, 0), Pos(1, 0), Pos(2, 0)], rot))


def Submarine(rot):
    return Ship("Submarine",
                rotate_shape([Pos(0, 0), Pos(1, 0), Pos(2, 0)], rot))


def Destroyer(rot):
    return Ship("Destroyer",
                rotate_shape([Pos(0, 0), Pos(1, 0)], rot))
