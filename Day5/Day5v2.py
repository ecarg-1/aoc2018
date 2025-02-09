import re
with open('input.txt','r') as f:
    string = f.read()
    f.close()
pattern = r''
for x in range(97,123): pattern += chr(x)+chr(x-32)+'|'+chr(x-32)+chr(x)+'|'

def react(string):
    prev = len(string)
    while True:
        string = re.sub(pattern, '', string)
        new = len(string)
        if new == prev: return new
        prev = new
    
print(react(string))