import re
import matplotlib.pyplot as plt
f = open('input.txt', 'r')
data = [[int(num) for num in item] for item in[re.findall(r'\d{1,7}|-\d{1,7}', line) for line in f.readlines()]]
for d in data: d[1], d[3] = d[1]*-1, d[3]*-1 #i am plotting where positive y goes up, the coordinates are given where positive y goes down so I made it go up
f.close()

def find_bounds(): #assumes that the starts will reach a minimum y boundary size when the letters show up
    y = [line[1] for line in data]
    min_y, max_y = min(y), max(y)
    return abs(min_y - max_y)

def move(): #moves each star based on velocity
    for line in data:
        line[0] += line[2]
        line[1] += line[3]

def unmove(): #unmoves the stars
    for line in data:
        line[0] -= line[2]
        line[1] -= line[3]

def plot(): #makes a plot
    x = [line[0] for line in data]
    y = [line[1] for line in data]
    plt.scatter(x ,y)
    plt.show()

min_bound = find_bounds()
ct = 0
while True:
    move()
    ct += 1
    cur_bound = find_bounds()
    min_bound = min(cur_bound, min_bound)
    if cur_bound > min_bound: 
        unmove()
        ct =- 1
        break
plot() #pt1 
print(ct) #pt2