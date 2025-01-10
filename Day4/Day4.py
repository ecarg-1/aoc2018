import re, statistics
with open('input.txt', 'r') as f:
    times_dict = {line[1:17]: line.strip('\n')[19:] for line in f.readlines()}
    f.close()
guards, sorted_times, fell_asleep_min = dict(), sorted(times_dict.keys()), 0                                    #guard dict, sorted times, time the current guard fell asleep
for time in sorted_times:                                                                                       #goes through times in order
    event = times_dict[time]                                                                                    #gets the event from the dict (ex: wakes up, falls asleep, new guard)
    match event:                                                                                                #matches event
        case 'wakes up':                                                                                        #if guard wakes up
            guards[cur_guard][1] += int(time[-2:]) - fell_asleep_min                                            #increments time spent asleep based on when guard fell asleep last
            guards[cur_guard][0] += [t for t in range(fell_asleep_min, int(time[-2:]))]                         #adds each minute they spent asleep to a list of all the minutes they were alseep for that hour
        case 'falls asleep': fell_asleep_min = int(time[-2:])                                                   #if guard falls asleep, notes the time
        case _:                                                                                                 #otherwise a new guard takes shift
            cur_guard = int(re.findall(r'\d{1,5}', event)[0])                                                   #find the guard number
            if cur_guard not in guards.keys(): guards[cur_guard] = [[], 0]                                      #if not in guard dict, adds them with a value list of times asleep, total time asleep
sleep_max, sleepiest_guard, sg_mode = 0, 0, 0                                                                   #maximum time spent asleep, sleepiest guard num, mode of sleepiest guard
cur_mode, mode_max, guard2, minute = 0, 0, 0, 0                                                                 #current mode for guard, max mode count, guard number for pt2, minute of the mode
for guard, value in guards.items():                                                                             #goes through guards
    if value[1] > sleep_max: sleep_max, sleepiest_guard, sg_mode = value[1], guard, statistics.mode(value[0])   #finds the sleepiest guard and the mode of the mins they spent asleep
    cur_mode = statistics.mode(value[0]) if value[0] else 0                                                     #current mode of guard (some guards didn't sleep so conditional statment needed)
    if value[0].count(cur_mode) > mode_max: mode_max, guard2, minute = value[0].count(cur_mode), guard, cur_mode#finds count of the mode to find the max
print(sleepiest_guard*sg_mode)                                                                                  #print pt1
print(guard2*minute)                                                                                            #print pt2