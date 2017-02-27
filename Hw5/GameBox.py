###### Gia tri Game
zombie_x = 3
px = 1
py = 3
bx = 5
by = 4
wx = 2
wy = 7

counts = 0
count1_x = 6
count1_y = 7
count2_x = 4
count2_y = 3

screen_height = 8
screen_width = 8


## Dieu kien check map
def in_map(x,y,screen_height,screen_width,):
    if x < 0 or y < 0  or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True
def in_box(bx , by, px, py):
    if (bx == px and by == py):
        return True
    return False

##### hien thi map
def move(x,y,dx,dy):
    return [x + dx, y + dy]

def index_map(screen_height, screen_width,bx, by,px,py,counts):
    for y in range(screen_height):
        for x in range(screen_width):
            if x == px and y == py:
                print("P", end=" ")
            elif x == bx and y == by:
                print("B", end=" ")
            elif x == wx and y == wy:
                print("*", end=" ")
            elif x == count1_x and y == count1_y:
                print("$", end=" ")
            elif x == count2_x and y == count2_y:
                print("$", end=" ")
            else:
                print(".", end=" ")
        print()
print(" Use W - S - A - D ")

while True:
        index_map(screen_height, screen_width, bx, by, px, py, counts)
        print("All point:", counts,"$")
        choice = input().upper()
    ### Dieu khien P
        dx = 0
        dy = 0
        if choice == "A":
             dx = -1
        elif choice == "D":
             dx = 1
        elif choice == "S":
             dy = 1
        elif choice == "W":
             dy = -1
        else:
            print("Change to: W - S - A - D")
    #### P vs B
        [next_px, next_py] = move(px, py, dx, dy)
        if in_box(bx, by, next_px, next_py):
            [next_bx, next_by] = move(bx, by, dx, dy)
            if not in_map(next_bx, next_by, screen_width, screen_height):
                print("Come Back , please!!!")
            else:
                bx = next_bx
                by = next_by
                px = next_px
                py = next_py
        else:
            if not in_map(next_px, next_py, screen_width, screen_height):
                print(" Can't Go!!!")
            else:
                px = next_px
                py = next_py

    ### An tien
        if px == count1_x and py == count1_y:
            counts += 1
            count1_x = screen_width +1
            count1_y = screen_height +1
            print("You have :+ ", counts ,"$")
        elif px == count2_x and py == count2_y:
            counts += 1
            count2_x = screen_width + 1
            count2_y = screen_height + 1
            print("You have :+ ", counts ,"$")
    ### Win
        if bx == wx and by == wy:
            counts += 10
            print("Good !!! YOu Win")
            print("Point: + 10 $")
            print("All Point: ", counts, "$")
            index_map(screen_height, screen_width, bx, by, px, py, counts)
            break

    ### close
        if bx == 0 and by == 0:
            print("Sorry ! You close")
            print("Point: ", counts, "$")
            break
        elif by == 0 and bx == screen_width -1 :
            print("Sorry ! You close")
            print("Point: ", counts, "$")
            break
        elif bx == 0 and bx == screen_height -1 :
            print("Sorry ! You close")
            print("Point: ", counts, "$")
            break
        elif bx == screen_width -1 and by == screen_height -1:
            print("Sorry ! You close")
            print("Point: ", counts, "$")
            break




