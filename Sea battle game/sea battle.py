from random import randint, choice

class Ship:
    def __init__(self, length, tp=1, x=None, y=None, is_move=True ):
        self._x, self._y = x, y
        self._length = length # 1,2,3,4
        self._tp = tp # 1- горизонтальная, 2 - вертикальная
        self._is_move = is_move
        self._cells = [1] * length
        self._coords = [(self._x, self._y)]

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        # перемещение корабля в направлении его ориентации
        if self._is_move == True:
            if self._tp == 1:
                if go == 1:
                    self._coords = [(x + 1, y) for x, y in self._coords]
                    self._x += 1
                elif go == -1:
                    self._coords = [(x - 1, y) for x, y in self._coords]
                    self._x -= 1
            elif self._tp == 2:
                if go == 1:
                    self._coords = [(x, y + 1) for x, y in self._coords]
                    self._y += 1
                elif go == -1:
                    self._coords = [(x, y - 1) for x, y in self._coords]
                    self._y -= 1

    def is_collide(self, ship):
        # проверка на столкновение с другим кораблем
        for coords1 in self._coords:
            for coords2 in ship._coords:
                if abs(coords1[0] - coords2[0]) <= 1 and abs(coords1[1] - coords2[1]) <= 1:
                    return True
        return False

    def is_out_pole(self, size):
        # проверка выхода из игрового поля
        x, y = self.get_start_coords()
        if self._tp == 1:
            if size - x < self._length:
                return True
        if self._tp == 2:
            if size - y < self._length:
                return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self._field = [[0 for i in range(self._size)] for j in range(self._size)]
        self._field_coords = [[(j,i) for i in range(self._size)] for j in range(self._size)]


    def check_ship_surroundings(self, ship):
        x, y = ship._coords[0]
        if self._field[y][x] == 1:
            return False
        for coords in ship._coords:
            x,y = coords[0], coords[1]
            lst = ((x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1,y),
                   (x + 1, y + 1))
            for coords2 in lst:
                try:
                    if self._field[coords2[1]][coords2[0]] == 1:
                        return False
                except:
                    continue
        return True


    def new_value(self, x,y, ship):
        ship.set_start_coords(x, y)
        if ship.is_out_pole(self._size):
            return False
        if ship._tp == 1:
            ship._coords = [(x + i, y) for i in range(ship._length)]
        elif ship._tp == 2:
            ship._coords = [(x, y + i) for i in range(ship._length)]
        return True

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1), Ship(1), Ship(1), Ship(1)]

        for ship in self._ships:
            while True:
                y, x = choice(choice(self._field_coords))
                if self.new_value(x, y, ship):
                    if self.check_ship_surroundings(ship):
                        for coords in ship._coords:
                            self._field[coords[1]][coords[0]] = 1
                            ind = [[i, j.index((coords[1],coords[0]))] for i, j in enumerate(self._field_coords) if (coords[1],coords[0]) in self._field_coords[i]]
                            del self._field_coords[ind[0][0]][ind[0][1]]
                        break

    def get_ships(self):
        return self._ships

    def move_ships(self):
        def check_coords(ship):
            if not ship.is_out_pole(self._size) and self.check_ship_surroundings(ship):
                return True

        for ship in self._ships:
            copy_coords = ship._coords[:]
            ship.move(1)
            if check_coords(ship):
                continue
            ship._coords = copy_coords[:]
            ship.move(-1)
            if not check_coords(ship):
                ship._coords = copy_coords[:]

    def show(self):
        for row in self._field:
            print(*row)

    def get_pole(self):
        return tuple(tuple(row) for row in self._field)




