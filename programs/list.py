def extendList(val, list=[]):
    list.append(val)
    return list

import pdb; pdb.set_trace()
list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print "list1 = %s" %list1
print "list2 = %s" %list2
print "list3 = %s" %list3
