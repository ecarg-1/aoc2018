players, last_marble_val = 405, 71700
# players, last_marble_val = 7, 25
from collections import deque, defaultdict
def run(players:int, last_marble:int):
    circle = deque([0])                                                 #double ended queue
    scores = defaultdict(int)                                           #will fill in any int as a valid key even if it doesn't yet exist
    for marble in range(1, last_marble + 1):
        if marble % 23 != 0:
            circle.rotate(-1)                                           #puts the first clockwise number at the end of the list
            circle.append(marble)                                       #adds the marble
        else:
            circle.rotate(7)                                            #puts the 7th ccw marble at the end
            scores[marble % players] += marble + circle.pop()           #does not matter if elf numbering starts at 0 or 1, pops the 7 ccw marble adds score with current marble num
            circle.rotate(-1)                                           #puts the current marble back at the end since the previous one got popped
    print(max(scores.values()))

run(players, last_marble_val)
run(players, last_marble_val * 100)



#Toooo slow
# cur_marble_ind, cur_marble_num = 0, 1
# marble_list = [0]
# elf_dict = {i : 0 for i in range(players)}
# cur_elf = 0
# def place_marble(marble_num:int, cur_marble_ind:int, elf_num:int) -> int:
#     length = len(marble_list)
#     if marble_num % 23 != 0:
#         new_marble_ind = (cur_marble_ind + 1) % length + 1
#         marble_list.insert(new_marble_ind, marble_num)
#     else:
#         new_marble_ind = (cur_marble_ind - 7) % length
#         removed_marble_num = marble_list.pop(new_marble_ind)
#         elf_dict[elf_num] += marble_num + removed_marble_num
#         print(elf_num, removed_marble_num,  marble_num)
#     return new_marble_ind

# while cur_marble_num <= last_marble_val: 
#     cur_marble_ind = place_marble(cur_marble_num, cur_marble_ind, cur_elf)
#     cur_marble_num += 1
#     cur_elf = (cur_elf + 1) % players

# print(max(elf_dict.values()))