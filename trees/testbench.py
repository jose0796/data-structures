
import sys
import time
from trees import * 

def __exit__(passed):
    sys.stdout.write("\033[1mTests passed " + str(passed) + "/7 \033[0;0m\n" )


n = 0
sys.stdout.write("\033[1;31m")
sys.stdout.write("Starting testbench on AVL implementation ")

sys.stdout.flush()

for i in range(3):
    time.sleep(0.5)
    sys.stdout.write(".")
    sys.stdout.flush()

sys.stdout.write("\033[0;0m")


sys.stdout.write("\ninstantiation test ...")


a = avl()


if type(a) == avl :
    sys.stdout.write("\033[1;32m passed. \033[0;0m\n")
    n += 1
else:
    sys.stdout.write("\033[1;31m failed. \n\033[0;0m")
    


#root
sys.stdout.write("insertion test ...")
a.insert(179)
a.insert(232)

if a.root.key == 179 and a.root.right.key == 232:
    sys.stdout.write("\033[1;32m passed. \033[0;0m\n")
    n += 1
else:
    sys.stdout.write("\033[1;31m failed. \n\033[0;0m")
    
print(a)



# left rotation test 
sys.stdout.write("left rotation test ...")


a.insert(525)

if a.root.key == 232:
    sys.stdout.write("\033[1;32m passed. \033[0;0m\n")
    n+=1
else:
    sys.stdout.write("\033[1;31m failed. \n\033[0;0m")
    

print(a)
#right rotation

sys.stdout.write("right rotation test ...")

a.insert(200)
a.insert(217)

if a.search(217).p.key == 200:
    sys.stdout.write("\033[1;32m passed. \033[0;0m\n")
    n +=1
else:
    sys.stdout.write("\033[1;31m failed. \n\033[0;0m")
    
print(a)

#LR rotation 

sys.stdout.write("left-right rotation test ...")

a.insert(301)
a.insert(429)

if a.search(301).p.key == 429  and a.search(525).p.key == 429:
    sys.stdout.write("\033[1;32m passed. \033[0;0m\n")
    n+=1
else:
    sys.stdout.write("\033[1;31m failed. \n\033[0;0m")
    

print(a)
#RL rotation

sys.stdout.write("right-left rotation test ...")

a.insert(229)
a.insert(223)


if a.search(229).p.key == 223  and a.search(217).p.key == 223:
    sys.stdout.write("\033[1;32m passed. \033[0;0m\n")
    n+=1
else:
    sys.stdout.write("\033[1;31m failed. \n\033[0;0m")
    
print(a)
#Deletion    

sys.stdout.write("deletion test ...")

a.delete(a.search(200))

x = a.search(217)


passed = True

if a.search(179).p.key != 217 or x.left.key != 179 or a.search(223).p.key != 217 or x.right.key != 223 or x.bf != 1: 
    passed = False


a.insert(219)

if a.search(219).p.key != 223 or a.search(223).left.key != 219 or a.search(223).bf != 0:
    passed = False

if passed:
    sys.stdout.write("\033[1;32m passed. \033[0;0m\n")
    n += 1
else:
    sys.stdout.write("\033[1;31m failed. \n\033[0;0m")
    
sys.stdout.write("\nResulting tree: \n")

print(a)


__exit__(n)
