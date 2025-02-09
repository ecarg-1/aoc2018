with open('input.txt', 'r') as f:
    string = f.read()
    f.close()

def react(string):
    new_string, i = '', 0
    while i < len(string):
        if i == len(string) - 1: new_string += string[i]
        elif abs(ord(string[i]) - ord(string[i+1])) != 32: new_string += string[i]
        else: i += 1
        i += 1
    return new_string
def run_reaction(string):
    prev = len(string)
    while True:
        string = react(string)
        new = len(string)
        if new == prev: break
        prev = new
    return prev
run_reaction(string) #pt1

min_len = len(string)
for x in range(97, 123):
    x = string.replace(chr(x),'').replace(chr(x-32),'')
    min_len = min(min_len, run_reaction(x))
print(min_len) #pt2 quite slow
