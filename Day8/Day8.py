f = open('input.txt','r')
nums = [int(x) for x in f.read().split()]
f.close()

active_children = []                                                                    #list of [active_children, metadata] which decrements active_children 
i = 0                                                                                   #index of numbers starts at 0
metadata_total = 0                                                                      #metadata total starts at 0
start_ends = []                                                                         #list of index pairs [start, end] (inclusive of both)
starts = []                                                                             #ongoing list of starts that have not yet found ends, starts removed once paired
while i < len(nums):                                                                    #loop until end of numbers is reached
    pair = nums[i:i+2]                                                                  #a pair is equal to the numbers in index i and i + 1
    if not active_children:                                                             #if there are no active children
        active_children.append(pair)                                                    #it adds the pair since it's the start
        starts.append(i)                                                                #starts a pair, appends index to starts
    elif active_children[-1][0] == 0:                                                   #if the last active children ct == 0
        metadata_total += sum(nums[i:i+active_children[-1][1]])                         #the following indicies are metadata and summed
        i += active_children[-1][1] - 2                                                 #increments i by the metadata length (-2 to account for normal inc)
        active_children = active_children[:-1]                                          #removes the child since it's no longer active
        start_ends.append([starts[-1], i + 1, nums[starts[-1] + 1]])                    #appends [start, end] to start_ends
        starts = starts[:-1]                                                            #removes the most recent start since it's done
    else:                                                                               #else the next pair is another child 
        active_children[-1][0] -= 1                                                     #decrements the previous child ct
        active_children.append(pair)                                                    #appends the new pair 
        starts.append(i)                                                                #adds a start index to starts
    i += 2                                                                              #inc by 2 each time since they're in pairs
print(metadata_total)                                                                   #print total (somehow I got the right answer the first time without having to change my code)
class Node:
    def __init__(self, info:list):
        self.info = info                #[start, end, children ct, metadata ct]
        self.start = info[0]            #start
        self.end = info[1]              #end
        self.metadata = info[2]         #metadata ct
        self.children = []              #list of child nodes starts empty
        self.parent = []                #parent node starts unknown
        self.score = None               #score starts unknown

    def find_parent(self, node_list):
        possible_parents = [node for node in node_list if node.start < self.start and node.end > self.end]
        if not possible_parents: self.parent = None
        else:
            parent_starts = [x.start for x in possible_parents]
            index = parent_starts.index(max(parent_starts))
            self.parent = possible_parents[index]
    
    def add_child(self, child):
        if child.parent == self: self.children.append(child)

    def score_node(self, num_line):
        if not self.children: self.score = sum(num_line[self.end + 1 - self.metadata:self.end + 1])
        else:
            child_scores = [child.score for child in self.children]
            if child_scores.count(None) == 0: #Ready to score
                metadata_ind = num_line[self.end + 1 - self.metadata:self.end + 1]
                self.score = sum(child_scores[i-1] for i in metadata_ind if i < len(child_scores) + 1 and i > 0)
            
nodes = [Node(data) for data in start_ends]

for node in nodes: node.find_parent(nodes)
parent = None
for node in nodes:
    if node.parent == None: parent = node
    for child in nodes:
        node.add_child(child)

while True:
    for node in nodes: node.score_node(nums)
    if parent.score: break
print(parent.score)