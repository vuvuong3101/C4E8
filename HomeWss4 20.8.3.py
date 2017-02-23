file=open("/Users/admin/Desktop/alice.txt","r")
file_name = file.read().split()
file.close()

sorted(file_name)

key=["you","have","alice","so","he","happy"]
def main(counts, character):
    count = 0
    
    for i in counts:
        if i.lower() == character.lower():
            count += 1
    return count
print("{0}:                {1}".format("word","Count"))
print("===========================") 
for it in key:
    n = main(file_name, it)
    print("{0}:                {1}".format(it, n))
  


