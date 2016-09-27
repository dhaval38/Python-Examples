import random

def display_list(l):
    print "**" 
    raw_input()


def bubblesort(l):
    for passesleft in range(len(l)-1, 0, -1):
        for index in range(passesleft):
            if l[index] < l[index + 1]:
                l[index], l[index+1] = l[index+1], l[index]
    display_list(l)

    return l

lt1 = [random.randrange(1, 50) for i in range(1, 20)]
print lt1
raw_input("")
import pdb; pdb.set_trace()
bubblesort(lt1)
print lt1        
