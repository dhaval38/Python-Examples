s = "Hacker Rank to Pythonistas"
new_s = ""
#s = list(s)
for item in s:
    if item.isupper():
        new_s += item.lower()
    else:
        new_s += item.upper()

print new_s
