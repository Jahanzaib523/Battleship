class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, rot):
        assert 0 <= rot <= 3
        if(rot == 0):
            return self
        else:
            for i in range(rot):
                temp = self.x
                self.x = self.y
                self.y = -1*temp
        return self


class Ship:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.hit = [0]*len(shape)

    def is_sunk(self):
        for i in range(len(self.hit)):
            if(self.hit[i] == 0):
                return False
        return True

    def hitHard(self, index):
        self.hit[index] = 1

    def print(self):
        s = ''
        for i in range(len(self.shape)):
            if(self.hit[i] == 0):
                s += self.name[0]
            else:
                s += "*"

        for i in range(10-len(self.shape)):
            s += ' '

        s += self.name
        print(s)


class Board:

    def __init__(self, size):
        assert 0 <= size
        self.size = size
        self.array = [' '*size]*size
        self.ships = []
        for i in range(size):
            for j in range(size):
                self.array[i] = self.array[i][:j] + '.' + self.array[i][j + 1:]

    def print(self):
        print('+', end='')
        for j in range(self.size*2):
            print('-', end='')
        print('-+\n')

        for i in range(self.size):
            print('|', end='')
            for j in range(self.size):
                print(' '+self.array[i][j], end='')
            print(' |\n')

        print('+', end='')
        for j in range(self.size*2):
            print('-', end='')
        print('-+\n')

# checks if pos is not interfering with other ships
    def getHit(self, pos):
        for i in range(len(self.ships)):
            for j in range(len(self.ships[i].shape)):
                if(self.ships[i].shape[j].x == pos.x and self.ships[i].shape[j].y == pos.y):
                    return True
        return False

    def add_ship(self, ship, position):
        list = []
        for i in range(len(ship.shape)):
            temp = Pos(ship.shape[i].x+position.x, ship.shape[i].y+position.y)
            assert 0 <= temp.x < self.size
            assert 0 <= temp.y < self.size
            list.append(temp)
            assert self.getHit(temp) == False

        ship.shape = list
        self.ships.append(ship)

        for i in range(len(list)):
            self.array[self.size-1-list[i].y] = self.array[self.size-1-list[i].y][:list[i].x] + \
                ship.name[0] + self.array[self.size -
                                          1-list[i].y][list[i].x + 1:]

    def has_been_used(self, pos):
        if(self.array[self.size-1-pos.y][pos.x] == '*' or self.array[self.size-1-pos.y][pos.x] == 'o'):
            return True
        return False

    def attempt_move(self, pos):
        assert 0 <= pos.x, pos.y < self.size
        assert self.has_been_used(pos) != True

        if(self.array[self.size-1-pos.y][pos.x] != '.'):
            self.array[self.size-1-pos.y] = self.array[self.size-1 -
                                                       pos.y][:pos.x] + "*" + self.array[self.size-1-pos.y][pos.x + 1:]
            self.setHit(pos)
            return 'hit'
        else:
            self.array[self.size-1-pos.y] = self.array[self.size-1 -
                                                       pos.y][:pos.x] + "o" + self.array[self.size-1-pos.y][pos.x + 1:]
            return 'miss'

    def setHit(self, pos):
        for i in range(len(self.ships)):
            for j in range(len(self.ships[i].shape)):
                if(self.ships[i].shape[j].x == pos.x and self.ships[i].shape[j].y == pos.y):
                    self.ships[i].hitHard(j)
                    return True
        return False
