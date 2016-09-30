from pexpect import *

if __name__ == "__main__":
    output = run('ls -la')
    print "output : %s" %output

    for i in range(3):
        child = spawn("sudo bash")
        child.expect(".*password\s*for\s*dhaval:")
        child.sendline("storage")
        child.expect("root@dhaval.*")
        print "Before : %s" %child.before  
        print "After : %s" %child.after  
        print "=========%s========" %i
