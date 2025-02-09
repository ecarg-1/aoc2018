f = open('input.txt', 'r') 
coords = [tuple(int(x[i]) for i in range(2)) for x in [line.strip('\n').split(', ') for line in f.readlines()]]     #list of tuples of releveant coordinates 
f.close()
def manhat_dist(a:tuple, b:tuple) -> int: return abs(a[0]-b[0]) + abs(a[1]-b[1])   #takes in coord a and coord b and returns the distance
def find_closest(c: tuple) -> tuple:    #takes in a coordinate and returns the closest relevant coordinate
    min_dist, closest, equal = 20000000, None, None
    for coord in coords:
        d = manhat_dist(c, coord)
        if d < min_dist: min_dist, closest = d, coord
        elif d == min_dist: equal = d
    if equal == min_dist: return None
    return closest

minx, miny, maxx, maxy = 1000, 1000, 0, 0                                                                       
for c in coords: minx, miny, maxx, maxy = min(c[0], minx), min(c[1], miny), max(c[0], maxx), max(c[1], maxy)    #finds the minmimum and maximum x and y coords
boundary = [(x, y) for y in [miny, maxy] for x in range(minx, maxx + 1)] + [(x, y) for x in [minx, maxx] for y in range(miny + 1, maxy)]    #list of boundary coordinates
infinite_coords = set() #coordinates that will have an infinite count
for bound in boundary: #any coordinate that has a closest coordinate on the boundary will be infinite 
    a = find_closest(bound)
    if a: infinite_coords.add(a)

dict_ct = {coord: 0 for coord in coords if coord not in infinite_coords}
for c in range(minx, maxx + 1):
    for r in range(miny, maxy + 1):
        closest = find_closest((c,r))
        if closest in dict_ct.keys(): dict_ct[closest] += 1

print(max(dict_ct.values())) #pt1 

def total_dist(c): return sum([manhat_dist(c, coord) for coord in coords])

#Assuming that we only have to check positive numbers 
col_flag, ct = False, 0
for x in range(maxx):
    row_flag = False
    for y in range(maxy):
        if total_dist((x,y)) < 10000: 
            ct += 1
            row_flag = True
    if row_flag: col_flag = True
    if col_flag and not row_flag: break
print(ct)   #pt2