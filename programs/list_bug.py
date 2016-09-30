list1 = [21, -9, 3, 98, 70, 2, 3, 67]
print "Original list : %s" %list1
#import pdb
#pdb.set_trace()
for item in list1:
    if item < 5:
        list1.remove(item)
        print list1

print "Final list : %s" %list1
