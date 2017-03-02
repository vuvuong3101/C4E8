# # p = {
# #     "x" : 2,
# #     "y" : 3
# }
### cach 2
p = {}
p["x"] = 2
p["y"] = 3
# b ={}
# b ["x"] = 3
# b ["y"] = 3

boxes = []
boxes.append({"x": 2, "y" : 4})
boxes.append({"x": 3 , "y": 2})
boxes.append({"x": 1 , "y": 4})

wins = []
wins.append({"x": 5, "y" : 5})
wins.append({"x": 1 , "y": 1})
wins.append({"x": 6 , "y": 2})


screen={}
screen["x"] = 7
screen["y"] = 7


def in_map(x, y, screen):
    if x < 0 or y < 0 or x > screen["x"] - 1 or y > screen["y"] - 1:
        return False
    return True

def check_match(objects, x, y): # check nhieu hop trong list
    for box in objects:
        if box["x"] == x and box["y"]== y:
            return True
    return False

def check_win(wins, x, y): # check nhieu hop trong list
    for win  in wins:
        if win["x"] == x and win["y"]== y:
            return True
    return False

def find_objects(objects,x ,y): #check vi tri box cham vao
    for object in objects:
        if object["x"] == x and object["y"] == y:
            return object
    return None


def move(x, y, dx, dy):
    return [x + dx, y + dy]


def print_map(dx,dy,p, win ,boxes,screen):
    for y in range(screen["y"]):
        for x in range(screen["x"]):
            if x == p["x"] and y == p["y"]:
                print("T ", end="")
            elif check_match(boxes,x,y):
                print("B ", end="")
            elif check_win(win, x , y):
                print("* ", end="")
            else:
                print("- ", end="")
        print()


while True:
    dx = 0
    dy = 0

    print_map(dx,dy,p , wins ,boxes, screen)
    choice = input("What do you want? U - D - L - R: ").upper()

    if choice == "W":
        dy = -1
    elif choice == "S":
        dy = 1
    elif choice == "A":
        dx = -1
    elif choice == "D":
        dx = 1

    [next_px, next_py] = move(p["x"], p["y"], dx, dy)
    if not in_map(next_px, next_py, screen):
        print("Go away!!")
    else:
        found_box = find_objects(boxes, next_px, next_py)
        if found_box is not None:
            next_bx = found_box["x"] + dx
            next_by = found_box["y"] + dy
            if not check_match(boxes, next_bx, next_by) and in_map(next_bx, next_by, screen):
                found_box["x"] += dx
                found_box["y"] += dy
                p["x"], p["y"] = next_px, next_py
        else:
            p["x"],p["y"] = next_px, next_py

    count_win = 0
    for box in boxes:
        for win in wins:
            if box["x"] == win["x"] and box["y"] == win["y"]:
                count_win += 1
    if count_win == len(wins) :
        print_map(dx, dy, p, wins, boxes, screen)
        print("you win")
        break