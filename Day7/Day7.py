f =  open('input.txt', 'r')
steps = [line.strip('\n').split() for line in f.readlines()]
f.close()

steps_dict = dict()
for step in steps:
    if step[-3] not in steps_dict.keys(): steps_dict[step[-3]] = [step[1]]
    else: steps_dict[step[-3]].append(step[1])
active_steps = sorted(list(set([step[1] for step in steps]) - set([step[-3] for step in steps])))

def pt1(active_steps):
    completed_steps, ever_active = [], set()
    while len(active_steps) != 0:
        completed_steps.append(active_steps[0])
        active_steps = active_steps[1:]
        for k in steps_dict.keys(): 
            if len(set(steps_dict[k]).intersection(set(completed_steps))) == len(steps_dict[k]) and k not in ever_active: active_steps.append(k)
        active_steps.sort()
        ever_active = ever_active.union(set(active_steps))
    print(''.join(completed_steps))
def pt2(active_steps):
    workers, t, completed_steps, ever_active = {i: [0, ''] for i in range(5)}, -1, [], set(active_steps)
    while(len(completed_steps)) != len(set([step[1] for step in steps]).union(set(step[-3] for step in steps))):
        t+=1
        for x in workers.keys():
            if workers[x][0] != 0: 
                workers[x][0] -= 1
                if workers[x][0] == 0: completed_steps.append(workers[x][1])
        for k in steps_dict.keys(): 
            if len(set(steps_dict[k]).intersection(set(completed_steps))) == len(steps_dict[k]) and k not in ever_active: active_steps.append(k)
        active_steps.sort()
        ever_active = ever_active.union(set(active_steps))
        for x in workers.keys():
            if workers[x][0] == 0 and len(active_steps) != 0: 
                workers[x][0], workers[x][1], active_steps = ord(active_steps[0]) - 4, active_steps[0], active_steps[1:]
    print(t)
pt1(active_steps.copy())
pt2(active_steps.copy())