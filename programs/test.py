import re
item = [ re.sub(r"\n$", "", line, re.I) for line in open("demo.txt", "r")]
print item, line
