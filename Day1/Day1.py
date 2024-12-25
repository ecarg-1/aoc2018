with open('input.txt','r') as f:
    steps = [int(line.strip('\n')) for line in f.readlines()]
    f.close()
print(sum(steps))#part1 

index, visited, cur_freq = 0, set(), 0 
while(True):
    index %= len(steps)
    cur_freq += steps[index]
    if cur_freq in visited: break
    else: visited.add(cur_freq)
    index+=1
print(cur_freq)
