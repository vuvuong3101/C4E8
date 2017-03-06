
class Player:
    def __init__(self,x ,y): # ham khoi tao
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
    def move_to(self,x,y):
        self.x = x
        self.y = y
    def calc_next(self,dx,dy):
        return ( self.x + dx , self.y + dy)
    def match(self ,x ,y):
        if self.x == x and self.y == y:
            self.text = "T"
            return True



# player = Player(3, 5) # = (player.x = 3 , player.y = 2)
# player.print()
# player.move(3, 0)
# player.print()
# print(player.calc_next(8, 10))
# player.move_to(9, 6)
# player.print()