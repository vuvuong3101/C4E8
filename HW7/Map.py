from person_player import Player
from box_map import Box
from  gate import Gate

class Map:
    def __init__(self, width, height):
        self.player = Player(3, 2)
        self.box = Box(2, 4)
        self.gate =  Gate(1, 3)
        self.width = width
        self.height = height



    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.player.match(x,y):
                    print(self.player.text, end=" ")
                elif self.box.match(x,y):
                    print(self.box.text, end=" ")
                elif self.gate.match(x, y):
                    print(self.gate.text, end=" ")
                else:
                    print("-", end=" ")
            print()
    def in_map(self, x , y ):
        if x < 0 or y < 0 or x > self.width -1 or y > self.height -1 :
            return True
        return False

    def move_box(self, dx, dy):
        self.box.move(dx, dy)

    def move_player(self, dx, dy):
        self.player.move(dx, dy)

    def process_input(self, move): # W S D A
        dx = 0
        dy = 0
        direction = move.upper()
        if direction == "W":
            dx, dy = 0, -1
        elif direction == "S":
            dx, dy = 0, 1
        elif direction == "A":
            dx, dy = -1, 0
        elif direction =="D":
            dx, dy = 1 , 0

        [next_px , next_py] = self.player.calc_next(dx, dy)

        if self.in_map(next_px,next_py):
            print(" Please, Come back")

        else:
            next_bx = self.box.x + dx
            next_by = self.box.y + dy
            if next_px == self.box.x and next_py == self.box.y:
                if self.in_map(next_bx, next_by):
                    print("NOT GO")
                else:
                    self.move_player(dx, dy)
                    self.move_box(dx, dy)

            else:
                self.move_player(dx, dy)




    def loop(self):
        while True:
            self.print()
            move = input("You move: W S A D")
            self.process_input(move)
            if self.box.x ==  self.gate.x  and self.box.y == self.gate.y:
                self.print()
                print(" YOU WIN !!")
                break
            elif self.box.x == 0 and self.box.y == 0:
                print("YOU LOSE")
                break
            elif self.box.x == 0 and self.box.y == self.height -1:
                print("YOU LOSE")
                break
            elif self.box.x == self.width -1 and self.box.y == 0:
                print("YOU LOSE")
                break
            elif self.box.x == self.width -1 and self.box.y == self.height -1:
                print("YOU LOSE")
                break

map = Map(6, 6)
map.loop()
