s_list= "homnaymangchanqua"
all_list= ["a","b","c","d","e","f","g","h","i","j"
           ,"k","l","m","n","o","p","q","r","s","t"
           ,"u","v","w","x","y","z"]
def count_s_list(list,letter) :
    count = 0
    for s in s_list:
            if s.lower() == letter.lower():
               count += 1
    return count
    print(count_s_list(list,letter))
    
for k in all_list:
    n = count_s_list(s_list, k)
    if n > 0:
        print("{0}: {1}".format(k,n))



###20.8.2
def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit]=quantity
    return
new_inventory = {}
add_fruit(new_inventory, "strawberries", 15)
print(new_inventory["strawberries"]==15)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"]==35)
