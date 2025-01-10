import re
with open('input.txt','r') as f:
    claims = [[int(c[i]) for i in range(len(c))] for c in [re.findall(r'\d{1,4}', line) for line in f.readlines()]]     #id, col, row, width, height intgers
    f.close()
def run(claimed_spots = set(), pt = 1, mult_claim = set()):                                                             #takes in by default an empty set (for recursion), part 1 (for recursion), and another empty set (to reduce lines of code)
    for claim in claims:
        spaces = [(c, r) for c in range(claim[1], claim[1] + claim[3]) for r in range(claim[2], claim[2] + claim[4])]   #list of tuples of all coordinates that a claim takes up
        overlap = False                                                                                                 #for pt2
        for space in spaces:                                                                                            #goes through each tuple
            if space in claimed_spots:                                                                                  #if space is already claimed
                mult_claim.add(space)                                                                                   #it goes into the multiupmultiplele claim set
                overlap = True                                                                                          #and overlap is true
            claimed_spots.add(space)                                                                                    #adds every spot to claimed spots set 
        if not overlap and pt==2: return f'Part 2: {claim[0]}'                                                          #for pt2, if a claim has no overlap, returns a string to be printed in the part 1 loops
    if pt == 1: print('Part 1:', len(mult_claim), run(mult_claim, 2))                                                   #for pt1 prints a count of how many at least double claims there were and prints pt2
run()