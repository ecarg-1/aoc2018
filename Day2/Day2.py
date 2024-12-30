with open('input.txt','r') as f:
    strings = [line.strip('\n') for line in f.readlines()]
    f.close()
def ct(string, num):
    chr_list = list(set([chr for chr in string]))
    for chr in chr_list: 
        if string.count(chr) == num: return True
    return False
def run():
    ct3, ct2 = 0, 0
    for s in strings:
        if ct(s, 2): ct2 += 1
        if ct(s, 3): ct3 += 1
    return ct2 * ct3
print(run())
#pt 2
for i in range(len(strings)-1):
    for j in range(i+1, len(strings)):
        mismatch_ct = 0
        pairs = [strings[i][k]+strings[j][k] for k in range(len(strings[i]))]
        for pair in pairs:
            if len(set(pair)) == 2: 
                pairs.remove(pair)
                mismatch_ct += 1
        if mismatch_ct == 1: print(''.join([p[0] for p in pairs]))

