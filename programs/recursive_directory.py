import os

def get_directory_contents(path):
    content = os.listdir(path)
    for item in content:
        childPath = os.path.join(path, item)
        if os.path.isdir(childPath):
            get_directory_contents(childPath)
        else:
            print childPath

def walk_directory_contents(path):
    for root, directory, _file in os.walk(path):
        print "root : %s" %root
        print "directory : %s" %directory
        print "file : %s" %_file

if __name__ == "__main__":
    #get_directory_contents("/home/dhaval/practice/python/examples")
    walk_directory_contents("/home/dhaval/practice/python")
        
