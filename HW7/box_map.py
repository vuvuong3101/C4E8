
class Box:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def match(self,box_x, box_y):
        if self.x == box_x and self.y == box_y:
            self.text = "B"
            return True

    def calc_next(self,dx,dy):
        return (self.x + dx, self.y + dy)

    def move(self,dx,dy):
        self.x += dx
        self.y += dy
