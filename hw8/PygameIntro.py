import pygame


pygame.init()
screen = pygame.display.set_mode([226, 226])
done = False

COLOR_WHITE =(255, 255, 255)

image_player = pygame.image.load("box.png")
square_image =  pygame.image.load("square.png")
box_image = pygame.image.load("mario.png")
gate_image = pygame.image.load("gate.png")
win_image = pygame.image.load("rsz_win.jpg")

class Gate:
    def __init__(self, x, y):
        [self.x, self.y] = [x, y]
class Box:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def calc_next(self, dx, dy):
        return [self.x + dx, self.y + dy]

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def calc_next(self,dx, dy):
        return[self.x + dx, self.y + dy]

class Map:
# khai bao cac phan tu game
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(1, 2)
        self.box = Box(3,5)
        self.gate = Gate(2,6)


# di chuyen cua game
    def move_game(self, dx, dy):
        [next_player_x, next_player_y] = self.player.calc_next(dx, dy)

        if not self.check_inside(next_player_x, next_player_y):
            print(" Please, Come back")

        else:
            [next_box_x, next_box_y] = [self.box.x + dx, self.box.y + dy]
            if next_player_x == self.box.x and next_player_y == self.box.y:
                if not self.check_inside(next_box_x, next_box_y):
                    print("NOT GO")
                else:
                    self.player.move(dx, dy)
                    self.box.move(dx, dy)

            else:
                self.player.move(dx, dy)

    def check_inside(self, x, y):
        if x < self.width and y < self.height and x >= 0 and y >= 0:
            return  True
        return  False


map = Map(7, 7)

x = 100
y = 100
SQUARE_SIZE = 32

# 
while not done:
    key_arrow = None
    dx = 0
    dy = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =  True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                dy = 1
            elif event.key ==  pygame.K_UP:
                dy = -1

    if dx != 0 or dy !=0:
        map.move_game(dx, dy)


    screen.fill(COLOR_WHITE) # ve background
    for y in range(map.height):
        for x in range(map.width):
            screen.blit(square_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))
    screen.blit(gate_image, (map.gate.x * SQUARE_SIZE, map.gate.y * SQUARE_SIZE))
    screen.blit(image_player, (map.box.x * SQUARE_SIZE, map.box.y * SQUARE_SIZE))

    screen.blit(box_image,(map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))# ve player
    if map.box.x == map.gate.x and map.box.y == map.gate.y:
        screen.blit(win_image,(0,0))
    pygame.display.flip() # fix lag