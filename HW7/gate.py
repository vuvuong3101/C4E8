class Gate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def match(self, x, y ):
        if self.x == x and self.y == y:
            self.text = "*"
            return True